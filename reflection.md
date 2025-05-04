# Reflection

Student Name:  Gwonwoo Cha
Sudent Email:  gcha01@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
Through this assignment, I was able to practice the entire process of collecting, cleaning, and transforming real-world data into an analyzable format. I used read_csv() and read_html() to extract data from Google Spreadsheets and the Numbeo website, and applied custom functions to preprocess dates and strings. I learned how important it is to standardize information such as country names, city names, and years, as inconsistencies in these fields can significantly affect analysis results. By adjusting salary data using the Cost of Living Index, I also realized the importance of context-aware analysis rather than relying solely on raw numbers. I used pivot tables to organize the final dataset by age group and education level, and uploaded the results to an S3-compatible cloud storage (MinIO), which gave me hands-on experience with building a basic data pipeline. The most challenging part was handling mismatches while merging data from different sources, which required a lot of debugging and edge case handling. Overall, this project gave me a broad, practical understanding of essential data analysis skills and how they can be applied in real-world scenarios.