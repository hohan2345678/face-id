from datetime import datetime
from pymongo import MongoClient
import pytz

print("connecting to db")
client = MongoClient("mongodb+srv://jakulerogod69:jakulerogods@jaja.uvxgo.mongodb.net/?retryWrites=true&w=majority&appName=jaja")

db = client["Attendance"]
collection = db["Student"]

print("loading data")
post1 = {"name": "Chris Laurence R. Briones", "grade_and_section": "12 Einstein", "lrn": "109229120472", "contact_number": "09294376808" }
post2 = {"name": "Johnloyd M. Cuentas", "grade_and_section": "12 Einstein", "lrn": "107532120008", "contact_number": "09055880910" }
post3 = {"name": "Jhetrocarl Ephraim P. Fernandez", "grade_and_section": "12 Einstein", "lrn": "109551120007", "contact_number": "09304363755" }
post4 = {"name": "John Andrei Kenneth S. Florendo", "grade_and_section": "12 Einstein", "lrn": "109667120083", "contact_number": "09519633509" }
post5 = {"name": "John Rex C. Inso", "grade_and_section": "12 Einstein", "lrn": "107536120041", "contact_number": "09853937939" }
post6 = {"name": "Kert Ryan A. Lumanta", "grade_and_section": "12 Einstein", "lrn": "109676140080", "contact_number": "09538102322" }
post7 = {"name": "Christian T. Malabanan", "grade_and_section": "12 Einstein", "lrn": "107538120024", "contact_number": "09933061078" }
post8 = {"name": "Nash R. Manzanero", "grade_and_section": "12 Einstein", "lrn": "107534120017", "contact_number": "0994824642" }
post9 = {"name": "Isael P. Matundan", "grade_and_section": "12 Einstein", "lrn": "108312120087", "contact_number": "09653693190" }
post10 = {"name": "Renzo C. Panes", "grade_and_section": "12 Einstein", "lrn": "107532130230", "contact_number": "09564016616" }
post11 = {"name": "Philip Josh Z. Reyes", "grade_and_section": "12 Einstein", "lrn": "107532120124", "contact_number": "09213298109" }
post12 = {"name": "John Carlo Q. Silva", "grade_and_section": "12 Einstein", "lrn": "107532120125", "contact_number": "09507985569" }
post13 = {"name": "Joevan V. Tejada", "grade_and_section": "12 Einstein", "lrn": "107528120028", "contact_number": "09159260602" }
post14 = {"name": "Dhaizel Ann J. Almayda", "grade_and_section": "12 Einstein", "lrn": "107532120050", "contact_number": "09453094213" }
post15 = {"name": "Kyl Nicole M. Bayanin", "grade_and_section": "12 Einstein", "lrn": "107535110007", "contact_number": "09303903224" }
post16 = {"name": "Monica R. Botes", "grade_and_section": "12 Einstein", "lrn": "107570120062", "contact_number": "09387888671" }
post17 = {"name": "Rhean Q. Canino", "grade_and_section": "12 Einstein", "lrn": "107535120039", "contact_number": "09944995348" }
post18 = {"name": "Reina Kryzanta M. Cave", "grade_and_section": "12 Einstein", "lrn": "107532140243", "contact_number": "09505037448" }
post19 = {"name": "Ryza Shiamelle R.  De Castro", "grade_and_section": "12 Einstein", "lrn": "423548150121", "contact_number": "09501743335" }
post20 = {"name": "Efephanie Shane M. De Gala", "grade_and_section": "12 Einstein", "lrn": "107306120088", "contact_number": "09619756883" }
post21 = {"name": "Avril Jade L. De Torres", "grade_and_section": "12 Einstein", "lrn": "107535120043", "contact_number": "09055880910" }
post22 = {"name": "Shane Elaisa O. De Torres", "grade_and_section": "12 Einstein", "lrn": "107538120043", "contact_number": "09859884529" }
post23 = {"name": "Shyne Ann S. Guiling", "grade_and_section": "12 Einstein", "lrn": "107435120045", "contact_number": "0998719370" }
post24 = {"name": "Jamaica B. Lopez", "grade_and_section": "12 Einstein", "lrn": "107532120001", "contact_number": "09568547439" }
post25 = {"name": "Ren Beatriz D. Magbuhos", "grade_and_section": "12 Einstein", "lrn": "401638150046", "contact_number": "09984710606" }
post26 = {"name": "Lhaire Kim A. Mendana", "grade_and_section": "12 Einstein", "lrn": "107528120047", "contact_number": "09123327274" }
post27 = {"name": "Kryzthal Gem P. Mercado", "grade_and_section": "12 Einstein", "lrn": "107428120078", "contact_number": "09304363755" }
post28 = {"name": "Jamela Mae M. Perez", "grade_and_section": "12 Einstein", "lrn": "107529120020", "contact_number": "09501722659" }
post29 = {"name": "Charlene Mae V. Ramos", "grade_and_section": "12 Einstein", "lrn": "107528120051", "contact_number": "09919497728" }
post30 = {"name": "Mary Rose D. Reyes", "grade_and_section": "12 Einstein", "lrn": "107528120053", "contact_number": "09953172805" }
post31 = {"name": "Sharmaine M. Sandoval", "grade_and_section": "12 Einstein", "lrn": "107575120068", "contact_number": "09852624040" }
post32 = {"name": "Joanna Joy D. Sotina", "grade_and_section": "12 Einstein", "lrn": "110169120391", "contact_number": "091669111146" }
post33 = {"name": "Nathalie Saicyu L. Vergara", "grade_and_section": "12 Einstein", "lrn": "10752710031", "contact_number": "09956095080" }
post34 = {"name": "Princess Gewell G. Villaraza", "grade_and_section": "12 Einstein", "lrn": "107526120087", "contact_number": "09533924728" }


insert_document = collection.insert_many([post1, post2,post3, post4, post5, post6, post7, post8, post9, post10, post11, post12, post13, post14, post15, post16, post17, post18, post19, post20, post21, post22, post23, post24, post25, post26, post27, post28, post29, post30, post31, post32, post33, post34])

print(f"Inserted Document ID: {insert_document.inserted_ids}")
client.close()


# App 1
# from model -> id
# look for a student with _id of id
# get student._id
# build attendance record
# {"student_id": student._id, "time": datetime.now(tz=pytz.timezone("PHT"))}
# Save to "Attendance" collections


# App 2
# TODAY
# Load all "Attendance" record where time >= datetime.combine(datetime.now(tz=pytz.timezone("PHT")), time.min)
# For each Attendance record, query the sstudent information by using student_id
# Display student infomation + Attendance.time
