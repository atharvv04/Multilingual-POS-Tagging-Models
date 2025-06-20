# POS Tagging Model Evaluation: CRF++ and HMM

## Overview:
This guide outlines the procedure to evaluate two different POS tagging models: Conditional Random Fields (CRF++) and Hidden Markov Models (HMM). The evaluation will be conducted on provided test datasets for both English and French languages. 

### I. CRF++ Model Evaluation

#### Steps:

1. **Acquire Training Data:**
   - Obtain the necessary training data for CRF++ model evaluation.

2. **Data Preprocessing:**
   - Parse the CoNLL files to extract tokens and POS tags.

3. **CRF++ Toolkit Installation:**
   - Download and unzip the CRF++ toolkit from its GitHub repository.

4. **Setting Up CRF++:**
   - Transfer the training data into the CRF++ toolkit folder.

5. **Template Design:**
   - Create a customized template to define feature constraints.
   - Define a specific template tailored to your constraints:
     ```plaintext
     # Unigram
     U00:%x[-1,0]
     U01:%x[0,0]
     U02:%x[1,0]
     ```
6. **Training:**
   - Train the CRF++ model using the training data and the defined template.
   ```plaintext
     % crf_learn template.txt <training_file_name> model
     ```

7. **Testing:**
   - Employ the trained model to perform tagging on the test dataset.
     ```plaintext
     % crf_test -m model <test_file>
     ```

8. **Evaluation Metrics:**
   - Develop Python code to compute accuracy, recall, and F1 score for model assessment.

Repeat these steps for both English and Marathi datasets.

### II. HMM Model Evaluation

#### Instructions:

1. **Acquire Training Data:**
   - Obtain the necessary training data for HMM model evaluation.

2. **Data Preprocessing:**
   - Parse the CoNLL files to extract tokens and POS tags.

3. **Model Implementation:**
   - Write Python code to create and train the HMM model.

4. **Testing:**
   - Utilize the trained model to tag the test dataset.

5. **Evaluation Metrics:**
   - Develop Python code to calculate accuracy, recall, and F1 score for model evaluation.

Repeat these steps for both English and Marathi datasets.

## Note:
Ensure to maintain consistency in data handling and evaluation procedures across both models. Accurate evaluation is crucial for assessing the performance of each model on different languages.
