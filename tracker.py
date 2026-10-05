# Job Application Tracker
# Keeps track of job applications and their status

import json

# Step 1: sample data
applications = [
    {"company": "Zoho", "role": "Python Developer", "status": "Applied", "application_date": "2026-09-02"},
    {"company": "Freshworks", "role": "Backend Engineer", "status": "Interview", "application_date": "2026-09-10"},
    {"company": "Infosys", "role": "Systems Engineer", "status": "Rejected", "application_date": "2026-08-18"},
    {"company": "Amazon", "role": "SDE Intern", "status": "Selected", "application_date": "2026-08-05"},
    {"company": "Razorpay", "role": "Software Engineer", "status": "Applied", "application_date": "2026-09-22"},
    {"company": "TCS", "role": "Data Analyst", "status": "Rejected", "application_date": "2026-08-25"},
]

statuses = ["Applied", "Interview", "Selected", "Rejected"]


# Step 2: core functions
def add_application(company, role, status, application_date):
    if status not in statuses:
        print("Invalid status:", status)
        return
    new_app = {
        "company": company,
        "role": role,
        "status": status,
        "application_date": application_date,
    }
    applications.append(new_app)


def search_by_status(status):
    result = []
    for app in applications:
        if app["status"] == status:
            result.append(app)
    return result


def search_by_company(company):
    result = []
    for app in applications:
        if app["company"].lower() == company.lower():
            result.append(app)
    return result


def update_status(company, new_status):
    if new_status not in statuses:
        print("Invalid status:", new_status)
        return
    for app in applications:
        if app["company"].lower() == company.lower():
            app["status"] = new_status
            return
    print("Company not found:", company)


# Step 3: summary
def get_summary():
    counts = {}
    for s in statuses:
        counts[s] = 0
    for app in applications:
        counts[app["status"]] += 1

    interview_list = []
    for app in applications:
        if app["status"] == "Interview":
            interview_list.append(app["company"] + " - " + app["role"])

    return counts, interview_list


# Step 4: save to a text file
def save_tracker(filename):
    counts, interview_list = get_summary()
    with open(filename, "w") as f:
        f.write("JOB APPLICATION TRACKER\n")
        f.write("=======================\n\n")
        f.write("Applications:\n")
        for app in applications:
            f.write(app["company"] + " | " + app["role"] + " | " +
                    app["status"] + " | " + app["application_date"] + "\n")

        f.write("\nSummary:\n")
        for s in statuses:
            f.write(s + ": " + str(counts[s]) + "\n")

        f.write("\nAt Interview stage:\n")
        if len(interview_list) == 0:
            f.write("None\n")
        for item in interview_list:
            f.write(item + "\n")


# save the sample data as a json file
with open("sample_applications.json", "w") as f:
    json.dump(applications, f, indent=2)

# testing the functions
add_application("Google", "Junior Developer", "Applied", "2026-09-28")
update_status("Zoho", "Interview")

print("Interview stage:", search_by_status("Interview"))
print("Zoho:", search_by_company("Zoho"))

counts, interview_list = get_summary()
print(counts)
print(interview_list)

save_tracker("tracker_report.txt")
print("Saved to tracker_report.txt")
