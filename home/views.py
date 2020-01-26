from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import MedicalRecords,PatientProfile,DoctorProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,'textured_blue\index.html')

def reports(request):
    records = MedicalRecords.objects.all()
    context = {'records':records}
    return render(request, r'textured_blue\reports.html', context)

def newReport(request):
    if request.method=='POST':
        pID = request.POST['pID']
        problem = request.POST['problem']
        date = request.POST['date']
        illness = request.POST['illness']
        comment = request.POST['comment']
        medicine = request.POST['medicine']
        duration = request.POST['duration']

        if ((not pID=="") and (not problem=="") and (not date=="") and (not illness=="") and
                (not comment=="") and (not medicine=="") and (not duration=="")):

            current_user = request.user
            doctor = DoctorProfile.objects.filter(user__id=4)
            patient = PatientProfile.objects.filter(user__id=pID)
            if (patient is not None):
                record = MedicalRecords.objects.create(patient=patient[0],doctor=doctor[0],problem=problem,date=date,
                                                   illness=illness,comment=comment,medicine=medicine,duration=duration)
                record.save()
                return redirect('index')
            else:
                return redirect('newReport')
    else:
        return render(request, r'textured_blue\new_report.html')