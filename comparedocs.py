import json
import spacy 
# Hello World program in Python
json1={
    # "college_name": null,
    "company_names": [
        "Bootstrap"
    ],
    "degree": [
        "BTech focused in Computer Science."
    ],
    "designation": [
        "Stack Developer",
        "Engineer",
        "Apex Coordinator",
        "Full-Stack Developer"
    ],
    "email": "rritikverma@gmail.com",
    "experience": [
        "Full-Stack Developer",
        "OST Talent private limited",
        
        "Php",
        "javascript",
        "monogDB",
        "MysQl",
        "python",
        "c",
        "jquery",
        "Skill",
        "Bootstrap",
        "semantic ui",
        "ui/ux design"
    ],
    "mobile_number": "7454948749",
    "name": "Ritik Verma",
    "no_of_pages": 1,
    "skills": [
        "English",
        "Apex",
        "Computer science",
        "Js",
        "Startup",
        "C",
        "Health",
        "Engineering",
        "Ux",
        "Ui",
        "Python",
        "Mysql",
        "Php",
        "Design",
        "Plan",
        "Javascript",
        "Algorithms",
        "Customer service",
        "Website",
        "System",
        "Seo",
        "Yoast",
        "Marketing"
    ],
    "total_experience": 0
}

json2={
    # "college_name": null,
    "company_names": [
        "Bootstrap"
    ],
    "degree": [
        "BTech focused in Computer Science."
    ],
    "designation": [
        "Stack Developer",
        "Engineer",
        "Apex Coordinator",
        "Full-Stack Developer"
    ],
    "email": "rritikverma@gmail.com",
    "experience": [
        "Full-Stack Developer",
        "OST Talent private limited",
       
        "Php",
        "javascript",
        "monogDB",
        "MysQl",
        "python",
        "c",
        "jquery",
        "Skill",
        "Bootstrap",
        "semantic ui",
        "ui/ux design"
    ],
    "mobile_number": "7454948749",
    "name": "Ritik Verma",
    "no_of_pages": 1,
    "skills": [
        "English",
        "Apex",
        "Computer science",
        "Js",
        "Startup",
        "C",
        "Health",
        "Engineering",
        "Ux",
        "Ui",
        "Python",
        "Mysql",
        "Php",
        "Design",
        "Plan",
        "Javascript",
        "Algorithms",
        "Customer service",
        "Website",
        "System",
        "Seo",
        "Yoast",
        "Marketing"
    ],
    "total_experience": 0
}

json1 = json.dumps(json1, sort_keys=True)
json2 = json.dumps(json2, sort_keys=True)

json1=''.join(e for e in json1 if e.isalnum())
json2=''.join(e for e in json2 if e.isalnum())

  
nlp = spacy.load('en_core_web_md') 
  
words = " ".join([json1.strip(), json2.strip()])
  
tokens = nlp(words) 
  
# for token in tokens: 
    # Printing the following attributes of each token. 
    # text: the word string, has_vector: if it contains 
    # a vector representation in the model,  
    # vector_norm: the algebraic norm of the vector, 
    # is_oov: if the word is out of vocabulary. 
    # print(token.text, token.has_vector, token.vector_norm, token.is_oov) 
  
token1, token2 = tokens[0], tokens[1] 
  
print("Similarity:", token1.similarity(token2)) 