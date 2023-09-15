# Customer Service Requests Analysis Project

In this GitHub repository, I've undertaken a comprehensive customer service requests analysis project. The goal was to gain valuable insights from a dataset containing customer complaints. Let's walk through the steps I've taken:

**Step 1: Importing and Reading Data**
I started by importing the dataset and thoroughly examining its contents to understand the columns and data structure.

**Step 2: Exploring Data Columns**
Next, I delved into the dataset's columns to gain a deeper understanding of the information they contain.

**Step 3: Converting Date Column**
To work with dates effectively, I converted the date column from its initial object format to a more suitable datetime format using a predefined function.

**Step 4: Adding a New "Month" Column**
I introduced a new column called "month" to categorize complaints based on the month they were reported.

**Step 5: Grouping Complaints by Date**
To identify any patterns, I grouped the complaints by date, shedding light on specific days with unusually high complaint counts.

**Step 6: Resetting and Renaming Columns**
To streamline the dataset and enhance readability, I reset and renamed columns as needed.

**Step 7: Visualizing Monthly Complaints**
I used a line graph to visualize the number of complaints per month, with a particular focus on June.

**Step 8: Further Column Adjustments**
Once again, I reset and renamed columns to ensure clarity in the dataset.

**Step 9: Bar Graph for Monthly Complaints**
To provide a clear overview, I created a bar graph to display the number of complaint records for each month.

**Step 10: Identifying Complaint Categories**
I identified complaint categories using the value_counts function and ensured consistent capitalization of category names.

**Step 11: Analyzing Complaint Categories**
Using a bar graph, I determined that the most common customer complaint category is "comcast."

**Step 12: Revisiting the Dataset**
I revisited the dataset to prepare for further analysis.

**Step 13-16: Identifying Complaints by Keywords**
I employed string operations to identify complaints containing specific keywords.

**Step 17: Examining "Status" Unique Values**
I explored the unique values within the "status" column.

**Step 18: Adjusting "Status" Column**
To facilitate analysis, I modified the "status" column based on specific conditions using if-else statements.

**Step 19: Understanding Complaint Status by State**
I determined the status of complaints by state, ensuring NaN values were appropriately handled.

**Step 20: Visualizing Complaint Status by State**
I used a bar plot to highlight that Georgia has the highest number of closed complaints.

**Step 21: Identifying Top Complaint States**
I identified the top complaint states using the value_counts function.

**Step 22: Revealing the State with the Most Unresolved Complaints**
Based on the data, I pinpointed the state with the highest number of unresolved complaints.

**Step 23: Calculating the Percentage of Unresolved Complaints**
I calculated the percentage of unresolved complaints in Georgia, which stood out as the most affected state.

**Step 24: Examining Resolved Complaints by "Received Via"**
Finally, I conducted an analysis to identify the percentage of complaints resolved via "customer care call" by grouping data based on "Received Via" and "New_Status" columns.

**Conclusion:**
In conclusion, my analysis revealed that approximately 50.62% of complaints have been successfully resolved through the "customer care call" channel. This project provided valuable insights into customer complaints, their resolution, and notable patterns related to complaint categories, states, and months.
