
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import IssueForm, ProfilePhotoForm
from .models import Issue, StatusUpdate
from django.contrib.auth import logout


@login_required
def home(request):
    profile = request.user.userprofile
    return render(request, "home.html", {"profile": profile})


@login_required
def profile(request):
    profile = request.user.userprofile
    issues = Issue.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "profile.html", {"profile": profile, "issues": issues})



@login_required
def upload_photo(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = ProfilePhotoForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfilePhotoForm(instance=profile)

    return render(request, "upload_photo.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user = authenticate(username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")


@login_required
def update_issue(request, pk):
    if not request.user.userprofile.is_admin:
        return redirect("home")

    issue = Issue.objects.get(id=pk)

    if request.method == "POST":
        status = request.POST["status"]
        note = request.POST["note"]

        issue.status = status
        issue.save()

        StatusUpdate.objects.create(issue=issue, status=status, note=note)

        return redirect("admin_dashboard")

    return render(request, "update_issue.html", {"issue": issue})


@login_required
def admin_dashboard(request):
    if not request.user.userprofile.is_admin:
        return redirect("home")  # Block access

    issues = Issue.objects.all().order_by('-created_at')
    return render(request, "admin_dashboard.html", {"issues": issues})



@login_required
def report_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()
            return redirect("issue_list")
    else:
        form = IssueForm()
    return render(request, "report_issue.html", {"form": form})

@login_required
def issue_list(request):
    issues = Issue.objects.filter(user=request.user)
    return render(request, "issue_list.html", {"issues": issues})


@login_required
def issue_detail(request, pk):
    issue = Issue.objects.get(id=pk)
    issue.refresh_from_db()
    updates = StatusUpdate.objects.filter(issue=issue).order_by('-updated_at')
    return render(request, "issue_detail.html", {"issue": issue, "updates": updates})


@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditUserForm(instance=user)

    return render(request, "edit_profile.html", {"form": form})



def logout_user(request):
    logout(request)
    return redirect("login")
