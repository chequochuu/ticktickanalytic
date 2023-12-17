import json
import csv
from datetime import datetime

def calculate_total_time(data):
    # Dictionary to hold total time for each task
    total_times = {}

    for entry in data:
        for task in entry['tasks']:
            # Extract task details
            title = task['title']
            start_time = datetime.fromisoformat(task['startTime'].replace('Z', '+00:00'))
            end_time = datetime.fromisoformat(task['endTime'].replace('Z', '+00:00'))

            # Calculate duration
            duration = end_time - start_time

            # Add duration to the total time of the task
            if title in total_times:
                total_times[title] += duration
            else:
                total_times[title] = duration

    return total_times

with open('ticktickdata.json', 'r') as file:
    data = json.load(file)

#For demonstration, using a variable 'data' (replace this with the above lines)
#data = [...]  # Your JSON data here

#Calculate total times
total_times = calculate_total_time(data)

#Print the results
for task, duration in total_times.items():
    print(f"Total time for '{task}': {duration}")



def calculate_duration(start_time, end_time):
    """Calculate the duration between two datetime objects."""
    start = datetime.fromisoformat(start_time.replace('Z', '+00:00'))
    end = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
    return end - start

def process_data_to_csv(data, csv_filename):
    """Process JSON data and write to a CSV file."""
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Task Title', 'Project Name', 'Start Time', 'End Time', 'Duration'])

        # Process each task and write to the CSV
        for entry in data:
            for task in entry['tasks']:
                duration = calculate_duration(task['startTime'], task['endTime'])
                writer.writerow([task['title'], task['projectName'], task['startTime'], task['endTime'], duration])

csv_filename = 'tasks_data.csv'

process_data_to_csv(data, csv_filename)
