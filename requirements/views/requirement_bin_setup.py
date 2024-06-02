

from requirements.forms.requirement_bin_form import CreateRequirementBin, EditRequirementBin
from django.http import JsonResponse, QueryDict
from django.shortcuts import redirect, render
import json
from django.contrib import messages
from utilities.forms.requirement_type_form import EditRequirementType
from utilities.models import RequirementCategory, RequirementType
from requirements.models import RequirementBin, RequirementBinContent, UserRequirementUpload
from django.utils import timezone
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

@login_required
def main(request, requirement_bin_id):
    state = 'active'
    serialized_state = json.dumps(state)
    records = RequirementBinContent.objects.select_related('requirement_bin').filter(is_deleted = False)
    deleted_records = RequirementBinContent.objects.select_related('requirement_type', 'requirement_bin').filter(is_deleted = True)
    requirement_bin = RequirementBin.objects.select_related('category').get(id=requirement_bin_id)
    categort_id = requirement_bin.category_id
    requirement_types = RequirementType.objects.select_related('category').filter(is_deleted=False, is_assigned_to_bin=False, category_id=categort_id)

    details = []
     # Iterate through each record and create an update form for it
    for record in records:
        update_form = EditRequirementType(instance=record)
        # created_by = record.created_by  # Get the user who created the record
        # modified_by = record.modified_by  # Get the user who modified the record
        details.append((record, update_form))


    context = {
        'requestz' : serialized_state , 
        'records': records,
        'deleted_records': deleted_records,
        'requirement_bin': requirement_bin,
        'requirement_bin_id': requirement_bin_id,
        'requirement_types': requirement_types,
        'details': details,
    }
    return render(request, 'requirement-bins-setup/main.html', context)


@login_required
@csrf_protect
def create(request, requirement_bin_id):
    if request.method == "POST":
        selected_record_ids = request.POST.getlist('selected_records')

        print('THE ID OF THE REQUIREMENT BIN: ' ,requirement_bin_id)

        if selected_record_ids:
            for record_id in selected_record_ids:
                requirement_type = RequirementType.objects.get(id=record_id)
                requirement_type.is_assigned_to_bin  = True
                requirement_type.save()

                RequirementBinContent.objects.create(
                    requirement_bin_id = requirement_bin_id,
                    requirement_type_id = record_id,
                    # created_by = request.user,
                )

                # Get the Requirement Bin record, this record is the parent record of the newly created record
                parent_record = RequirementBin.objects.get(id=requirement_bin_id)
                parent_record.has_child_records = True                              #Mark this as True since we created a child record, it only indicates that this record has child records
                parent_record.save()                                                #Save it to the database


            messages.success(request, f'Requirement Types is successfully added!') 
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({'error': 'There is nothing to add. Please select a requirement type before clicking the add button.'}, status=404)
    


@login_required
@csrf_protect
def soft_delete(request):
    if request.method == "POST":
        pk = request.POST.get('primary-key')   
        try:
            record = RequirementBinContent.objects.get(id=pk)

            #After getting that record, this code will delete it.
            # record.modified_by = request.user
            record.deleted_at = timezone.now()
            record.is_deleted=True

            #Get the foreign ids of the parent tables
            requirement_bin_id = record.requirement_bin_id    

            print(requirement_bin_id)  
  
                                            
              #Save it to the database
            record.save()
       

            messages.success(request, f'The requirement type is successfully removed from the list!') 
            return redirect('requirements:requirement-bin-setup', requirement_bin_id)
        except RequirementBin.DoesNotExist:
            return JsonResponse({'errors': 'Requirement record not found. Please try again.'}, status=404)


@login_required
@csrf_protect
def restore(request):
    if request.method == 'POST':
        selected_record_ids = request.POST.getlist('selected_deleted_records')  

        if selected_record_ids:
            for record_id in selected_record_ids:
                try:
                    record = RequirementBinContent.objects.get(pk=record_id)
                    record.is_deleted = False
                    record.deleted_at = None
                    # record.modified_by = request.user.id
                    record.save()
                except RequirementBinContent.DoesNotExist:
                    pass  # Handle cases where record might not exist

            messages.success(request, f'Deleted Records is successfully restored!') 
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({'error': 'There is nothing to restore. Please select a record to restore.'}, status=404)
    
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=404)
          

@login_required
@csrf_protect
def hard_delete(request):
    if request.method == 'POST':

        pk = request.POST.get('primary-key')  

        # data = QueryDict(request.body.decode('utf-8'))
        # entered_password = data.get('password')
        # user = request.user

        # if user and user.is_authenticated:
        #     if authenticate(email=user.email, password=entered_password):
                # Gets the records who have this ID
            

        child_record = UserRequirementUpload.objects.filter(requirement_bin_content_id = pk).exists() 
        if child_record:
            child_record_counts = UserRequirementUpload.objects.filter(requirement_bin_content_id = pk)
            return JsonResponse({'success': False, 'error': f'Unable to delete. This record has {child_record_counts} child records. To delete, first remove the child records.'})

        # else:
        record = RequirementBinContent.objects.get(id=pk) #Get the record using the value of the pk
        requirement_bin_id = record.requirement_bin_id #Get the requirement bin id from the record
        requirement_type_id = record.requirement_type_id
        record.delete() #After getting that record, this code will delete it.


        # Check if there are existing child records referenced to the requirement bin record
        requirement_bin_content_exist = RequirementBinContent.objects.filter(requirement_bin_id = requirement_bin_id).exists()

        if requirement_bin_content_exist == False:                                  #If there is no exising child records, run the below codes
            requirement_bin = RequirementBin.objects.get(id=requirement_bin_id)     #Get the requirement bin record using the requirement_bin_id
            requirement_bin.has_child_records = False                               #Mark the has_child_records to False since it has no child records
            requirement_bin.save()                                                  #Save it to the database


        # Reinitialized the variable to none
        requirement_bin_content_exist = None

        # Check if there are existing child records referenced to the requirement type record
        requirement_bin_content_exist = RequirementBinContent.objects.filter(requirement_type_id = requirement_type_id).exists()

        if requirement_bin_content_exist == False:                                  #If there is no exising child records, run the below codes
            requirement_type = RequirementType.objects.get(id=requirement_type_id)  #Get the requirement type record using the requirement_bin_id
            requirement_type.has_child_records = False                              #Mark the has_child_records to False since it has no child records
            requirement_type.is_assigned_to_bin  = False                            #Mark the is_assigned_to_bin to False since it is no longer assigned to the requirement bin
            requirement_type.save()                                                 #Save it to the database

        messages.success(request, f'The Requirement Type is permanently deleted!') 
        return JsonResponse({'success': True}, status=200)
    
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
    


# def hard_delete(request, pk):
#     if request.method == 'POST':

#         # data = QueryDict(request.body.decode('utf-8'))
#         # entered_password = data.get('password')
#         # user = request.user

#         # if user and user.is_authenticated:
#         #     if authenticate(email=user.email, password=entered_password):
#                 # Gets the records who have this ID

#         child_record = RequirementType.objects.filter(category_id = pk).exists() 
#         if child_record:
#             child_record_counts = RequirementType.objects.filter(category_id = pk).count()
#             return JsonResponse({'success': False, 'error': f'Unable to delete. This record has {child_record_counts} child records. To delete, first remove the child records.'})

#         else:
#             category_record = RequirementCategory.objects.get(id=pk)
#             #After getting that record, this code will delete it.
#             parent_id = category_record.semester_id
#             category_record.delete()

#             # Check if the parent records has a child records
#             new_record = RequirementCategory.objects.filter(semester_id = parent_id).exists() 

#             # If there is no child record, then get the parent record and change the has_child_records to False
#             if new_record == False:
#                 parent_record = Semester.objects.get(id = parent_id)

#                 parent_record.has_child_records = False
#                 parent_record.save()

#             messages.success(request, f'Requirement Category is permanently deleted!') 
#             return JsonResponse({'success': True}, status=200)
    
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request'})


# def hard_delete(request, pk):
#     if request.method == 'DELETE':

#         data = QueryDict(request.body.decode('utf-8'))
#         entered_password = data.get('password')
#         user = request.user

#         if user and user.is_authenticated:
#             if authenticate(email=user.email, password=entered_password):

#                 child_record = Semester.objects.filter(school_year_id = pk).exists() 
#                 if child_record:
#                     child_record_counts = Semester.objects.filter(school_year_id = pk).count()
#                     return JsonResponse({'success': False, 'error': f'Unable to delete. This record has {child_record_counts} child records. To delete, first remove the child records.'})

#                 else:
#                     record = Semester.objects.get(id=pk)
#                     #After getting that record, this code will delete it.
#                     record.delete()
#                     messages.success(request, f'School Year is permanently deleted!') 
#                     return JsonResponse({'success': True}, status=200)

#             else:
#                 return JsonResponse({'success': False, 'error': 'Incorrect password'})
#         else:
#             return JsonResponse({'success': False, 'error': 'User not logged in'})

#     return JsonResponse({'success': False, 'error': 'Invalid request'})


    


# @login_required
# def update(request, pk):
#     # Retrieve the type object with the given primary key (pk)
#     try:
#         accreditation_body = accredbodies.objects.get(id=pk)
#     except type.DoesNotExist:
#         return JsonResponse({'errors': 'Acrreditation body not found'}, status=404)

#     # Create an instance of the form with the type data
#     # update_form = Create_Bodies_Form(instance=type)
#     if request.method == 'POST':
#         # Process the form submission with updated data
#         update_form = Create_Bodies_Form(request.POST or None, instance=accreditation_body)
#         if update_form.is_valid():
#             # Save the updated data to the database
#             update_form.instance.modified_by = request.user
#             update_form.save()
#             abbreviation = update_form.cleaned_data.get('abbreviation')

#             # Provide a success message as a JSON response
#             messages.success(request, f'{abbreviation} is successfully updated!') 

#             return JsonResponse({"status": "success"}, status=200)

#         else:
#             # Return a validation error as a JSON response
#             return JsonResponse({'errors': update_form.errors}, status=400)
        

# @login_required
# def soft_delete(request, pk):
#     # Gets the records who have this ID
#     accreditation_body = accredbodies.objects.get(id=pk)

#     #After getting that record, this code will delete it.
#     accreditation_body.modified_by = request.user
#     accreditation_body.deleted_at = timezone.now()
#     accreditation_body.is_deleted=True
#     abbreviation = accreditation_body.abbreviation
#     accreditation_body.save()
#     messages.success(request, f'{abbreviation} accreditation bodies is successfully archived!') 
#     return redirect('accreditations:bodies-landing')


# @login_required
# def restore_bodies(request, pk):
#     # Gets the records who have this ID
#     accreditation_body = accredbodies.objects.get(id=pk)

#     #After getting that record, this code will restore it.
#     accreditation_body.modified_by = request.user
#     accreditation_body.deleted_at = None
#     accreditation_body.is_deleted=False
#     abbreviation = accreditation_body.abbreviation
#     accreditation_body.save()
#     messages.success(request, f'{abbreviation} accreditation bodies is successfully restored!') 
#     return redirect('accreditations:bodies-archive-page')



# @login_required
# def hard_delete(request, pk):
#     if request.method == 'DELETE':

#         data = QueryDict(request.body.decode('utf-8'))
#         entered_password = data.get('password')
#         user = request.user

#         if user and user.is_authenticated:
#             if authenticate(email=user.email, password=entered_password):
#                 # Gets the records who have this ID
#                 accreditation_bodies = accredbodies.objects.get(id=pk)

#                 #After getting that record, this code will delete it.
#                 accreditation_bodies.delete()
#                 messages.success(request, f'Accreditation Body is permanently deleted!') 
#                 url_landing = "/accreditation/bodies/archive_page/"
#                 return JsonResponse({'success': True, 'url_landing': url_landing}, status=200)
            
#             else:
#                 return JsonResponse({'success': False, 'error': 'Incorrect password'})
#         else:
#             return JsonResponse({'success': False, 'error': 'User not logged in'})

#     return JsonResponse({'success': False, 'error': 'Invalid request'})



