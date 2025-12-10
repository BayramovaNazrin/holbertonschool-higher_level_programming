#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Input type validation
    if not isinstance(template, isinstance(template, str).__class__):
        print("Invalid input: template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # Empty template check
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # Empty attendees check
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        processed = template[:]  # make a copy of the template

        # Replace each placeholder
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key) if attendee.get(key) else "N/A"
            processed = processed.replace("{" + key + "}", value)

        # Write output file
        filename = f"output_{idx}.txt"
        
        try:
            with open(filename, "w") as file:
                file.write(processed)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
