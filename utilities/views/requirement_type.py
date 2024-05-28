

from utilities.forms.requirement_type_form import CreateRequirementType, EditRequirementType
from django.http import JsonResponse, QueryDict
from django.shortcuts import redirect, render
import json
from django.contrib import messages
from utilities.models import RequirementCategory, RequirementType
from utilities.views.semester import *
from django.utils import timezone
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect


def main(request, category_id):
    state = 'active'
    serialized_state = json.dumps(state)
    create_form = CreateRequirementType(request.POST or None)
    records = RequirementType.objects.select_related('category').filter(is_deleted = False, category_id=category_id)
    deleted_records = RequirementType.objects.select_related('category').filter(is_deleted = True, category_id=category_id)
    requirement_category = RequirementCategory.objects.select_related('semester').get(id=category_id)

    # Initialize an empty list to store update forms for each record
    details = []

    # Iterate through each record and create an update form for it
    for record in records:
        update_form = EditRequirementType(instance=record)
        # created_by = record.created_by  # Get the user who created the record
        # modified_by = record.modified_by  # Get the user who modified the record
        details.append((record, update_form))

    context = {
        'requestz' : serialized_state , 
        'create_form': create_form,
        'records': records,
        'details': details,
        'deleted_records': deleted_records,
        'category_id': category_id,
        'requirement_category': requirement_category 
    }
    return render(request, 'requirement-types/main.html', context)


# @login_required
@csrf_protect
def create(request):
    create_form = CreateRequirementType(request.POST or None)
    if create_form.is_valid():
        category_id = request.POST.get('category_id')  
        # create_form.instance.created_by = request.user
        create_form.instance.category_id = category_id
        create_form.save()

        new_instance = create_form.save()
        parent_id = new_instance.category_id  # Get the IDcreate_form.save()

        parent_record = RequirementCategory.objects.get(id=parent_id)
        parent_record.has_child_records = True
        parent_record.save()

        messages.success(request, f'New Requirement Type is successfully added!') 
        return JsonResponse({'success': True }, status=200)

    else:
        # Return a validation error using a JSON response
        return JsonResponse({'errors': create_form.errors}, status=400)
    


# @login_required
@csrf_protect
def edit(request, pk):
    # Retrieve the type object with the given primary key (pk)
    try:
        record = RequirementType.objects.get(id=pk)
        # Get the old parent ID
        old_parent_id = record.category_id
    except RequirementType.DoesNotExist:
        return JsonResponse({'errors': 'Requirement Type record not found. Please try Again'}, status=404)

    # Create an instance of the form with the type data
    # update_form = Create_Bodies_Form(instance=type)
    if request.method == 'POST':
        # Process the form submission with updated data
        update_form = EditRequirementType(request.POST or None, instance=record)
        if update_form.is_valid():
            # Save the updated data to the database
            # update_form.instance.modified_by = request.user

    
            new_instance = update_form.save()
            new_parent_id = new_instance.category_id 
            
            
            print(old_parent_id, '==', new_parent_id)             # After saving, get the new parent ID

            # CHECK IF THE PARENT IDS ARE NOT EQUAL
            if old_parent_id != new_parent_id:
                print('HINDI SILA EQUAL PARE')
                parent_record = RequirementCategory.objects.get(id=new_parent_id)
                # Change the has_child_records of the new parent in to True
                parent_record.has_child_records = True
                parent_record.save()


                # Query the database if there is a child record for the old parent record
                is_have_child_records = RequirementType.objects.filter(category_id = old_parent_id).exists()

                # Check if there is no child records existing
                if is_have_child_records == False:
                    old_parent_record = RequirementCategory.objects.get(id=old_parent_id)    # Get the old parent record
                    old_parent_record.has_child_records = False                     # Change it to False since there is no child records existing
                    old_parent_record.save()                                        # Save it to the database
                    

            # Provide a success message as a JSON response
            messages.success(request, f'Requirement Type is successfully updated!') 
            return JsonResponse({"status": "success"}, status=200)

        else:
            # Return a validation error as a JSON response
            return JsonResponse({'errors': update_form.errors}, status=400)
        

# @login_required
@csrf_protect
def soft_delete(request):
    if request.method == "POST":
        pk = request.POST.get('primary-key')  

        try:
            record = RequirementType.objects.get(id=pk)
            category_id = record.category_id
            #After getting that record, this code will delete it.
            # record.modified_by = request.user
            record.deleted_at = timezone.now()
            record.is_deleted=True
            record.save()
            messages.success(request, f'The record is successfully deleted!') 
            return redirect('utilities:requirement-type', category_id)
        except RequirementType.DoesNotExist:
            return JsonResponse({'errors': 'Requirement Type record not found. Please try Again'}, status=404)


# @login_required
@csrf_protect
def restore(request):
    if request.method == 'POST':
        selected_record_ids = request.POST.getlist('selected_records')  

        if selected_record_ids:
            for record_id in selected_record_ids:
                try:
                    record = RequirementType.objects.get(pk=record_id)
                    record.is_deleted = False
                    record.deleted_at = None
                    # record.modified_by = request.user.id
                    record.save()
                except RequirementType.DoesNotExist:
                    pass  # Handle cases where record might not exist

            messages.success(request, f'Deleted Records is successfully restored!') 
            return JsonResponse({"status": "success"}, status=200)
        else:
            return JsonResponse({'error': 'There is nothing to restore. Please select a record to restore.'}, status=404)
    
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=404)
          

# @login_required
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
            

        # child_record = RequirementBin.objects.filter(category_id = pk).exists() 
        # if child_record:
        #     child_record_counts = RequirementBin.objects.filter(category_id = pk).count()
        #     return JsonResponse({'success': False, 'error': f'Unable to delete. This record has {child_record_counts} child records. To delete, first remove the child records.'})

        # else:
        record = RequirementType.objects.get(id=pk)
        #After getting that record, this code will delete it.
        record.delete()
        messages.success(request, f'Requirement Category is permanently deleted!') 
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



