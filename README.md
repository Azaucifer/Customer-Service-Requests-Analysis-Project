# ☎️ Comcast Telecom Consumer Complaints

## 📜 Overview
This project aims to analyze and visualize consumer complaints about Comcast, a US-based telecommunications company. The goal is to gain insights into the company's performance and identify common issues faced by customers. By examining the data, we can better understand the nature of complaints, their frequency, and how they are resolved.

## 🗂 Features
Our analysis includes the following features:
- **Complaint Trends**: Visualize the number of complaints over time, both monthly and daily.
- **Complaint Types**: Identify the most common types of complaints, such as internet issues, billing problems, and customer service.
- **State-wise Analysis**: Provide insights into which states have the highest number of complaints and unresolved issues.
- **Resolution Status**: Analyze the percentage of complaints that have been resolved versus those that remain open.
- **Communication Channels**: Examine how complaints were received (e.g., via the internet, customer care calls).

## 📈 Customer Service Requests Analysis Project
In this GitHub repository, I've undertaken a comprehensive customer service requests analysis project. The goal was to gain valuable insights from a dataset containing customer complaints. Let's walk through the steps I've taken:

### 📝 Step-by-Step Process
1. **Importing and Reading Data**: I started by importing the dataset and thoroughly examining its contents to understand the columns and data structure.
2. **Exploring Data Columns**: Next, I delved into the dataset's columns to gain a deeper understanding of the information they contain.
3. **Converting Date Column**: To work with dates effectively, I converted the date column from its initial object format to a more suitable datetime format using a predefined function.
4. **Adding a New "Month" Column**: I introduced a new column called "month" to categorize complaints based on the month they were reported.
5. **Grouping Complaints by Date**: To identify any patterns, I grouped the complaints by date, shedding light on specific days with unusually high complaint counts.
6. **Resetting and Renaming Columns**: To streamline the dataset and enhance readability, I reset and renamed columns as needed.
7. **Visualizing Monthly Complaints**: I used a line graph to visualize the number of complaints per month, with a particular focus on June.
8. **Further Column Adjustments**: Once again, I reset and renamed columns to ensure clarity in the dataset.
9. **Bar Graph for Monthly Complaints**: To provide a clear overview, I created a bar graph to display the number of complaint records for each month.
10. **Identifying Complaint Categories**: I identified complaint categories using the value_counts function and ensured consistent capitalization of category names.
11. **Analyzing Complaint Categories**: Using a bar graph, I determined that the most common customer complaint category is "comcast."
12. **Revisiting the Dataset**: I revisited the dataset to prepare for further analysis.
13. **Identifying Complaints by Keywords**: I employed string operations to identify complaints containing specific keywords.
14. **Examining "Status" Unique Values**: I explored the unique values within the "status" column.
15. **Adjusting "Status" Column**: To facilitate analysis, I modified the "status" column based on specific conditions using if-else statements.
16. **Understanding Complaint Status by State**: I determined the status of complaints by state, ensuring NaN values were appropriately handled.
17. **Visualizing Complaint Status by State**: I used a bar plot to highlight that Georgia has the highest number of closed complaints.
18. **Identifying Top Complaint States**: I identified the top complaint states using the value_counts function.
19. **Revealing the State with the Most Unresolved Complaints**: Based on the data, I pinpointed the state with the highest number of unresolved complaints.
20. **Calculating the Percentage of Unresolved Complaints**: I calculated the percentage of unresolved complaints in Georgia, which stood out as the most affected state.
21. **Examining Resolved Complaints by "Received Via"**: Finally, I conducted an analysis to identify the percentage of complaints resolved via "customer care call" by grouping data based on "Received Via" and "New_Status" columns.

### 📎 Conclusion
In conclusion, my analysis revealed that approximately 50.62% of complaints have been successfully resolved through the "customer care call" channel. This project provided valuable insights into customer complaints, their resolution, and notable patterns related to complaint categories, states, and months.

## 🔮 Purpose
The purpose of this project is to provide a comprehensive analysis of Comcast Telecom Consumer Complaints and customer service requests, helping stakeholders understand the key issues faced by customers. By identifying trends and patterns, the project aims to support efforts to improve customer service and address common problems effectively.

## 🪧 How to Use
1. **Download**: Download the dataset and any associated files from the repository.
2. **Open Data**: Load the data into your preferred analysis tool (e.g., Python, R).
3. **Run Analysis**: Use the provided scripts to perform the analysis and generate visualizations.
4. **Explore Results**: Review the generated charts and tables to gain insights into Comcast's consumer complaints.

Thank you for using the Comcast Telecom Consumer Complaints and Customer Service Requests Analysis Project. We hope you find the insights valuable for improving customer satisfaction and service quality.
