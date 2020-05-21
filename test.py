from pyresparser import ResumeParser
data = ResumeParser('/home/ritik/Desktop/ritik-auth/RitikVerma.pdf').get_extracted_data()
print(data)