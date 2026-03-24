import os


def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if (not isinstance(attendees, list) or
            not all(isinstance(a, dict) for a in attendees)):
        print("Error: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        content = template

        placeholders = ["name", "event_title", "event_date", "event_location"]

        for j in placeholders:

            valeur = attendee.get(j)
            if valeur is None:
                valeur = "N/A"

            content = content.replace(f"{{{j}}}", str(valeur))
        filename = f"output_{i}.txt"

        if os.path.exists(filename):
            print(f"File {filename} already exists")

        try:
            with open(filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error {filename}: {e}")
