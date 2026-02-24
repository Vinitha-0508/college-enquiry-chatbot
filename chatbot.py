def get_response(user_input):
    user_input = user_input.lower()
    words = user_input.split()  # split into words to avoid "hi" in "which"
    # ---------------------- University / Affiliation ----------------------
    if any(keyword in user_input for keyword in [
        "university", 
        "which university", 
        "college belongs to which university",
        "affiliated university",
        "university affiliation",
        "which university is this college under",
        "university details",
        "which university is this"
    ]):
        return "Our college is affiliated with Bharathiar University."

    # ---------------------- UG / PG / Courses ----------------------
    elif "ug" in user_input:
        return (" The college offeres 9 ug programmes: B.Com: General, Computer Applications, Banking and Insurance.\n"
                "B.Sc: Computer Science, Mathematics, Chemistry, Costume Design and Fashion.\n"
                "BA: English Literature, Tamil Literature.")

    elif "pg" in user_input:
        return "M.Sc: Computer Science."

    elif "bsc" in user_input or "b.sc" in user_input:
        return "BSc Computer Science, BSc Mathematics, BSc Chemistry, BSc Costume Design & Fashion."

    elif "b.com" in user_input or "b com" in user_input:
        return "B.Com, B.Com Computer Application, B.Com Banking & Insurance."

    elif "ba" in user_input or "b.a" in user_input:
        return "BA Tamil, BA English."

    elif "msc" in user_input or "m.sc" in user_input:
        return "MSc Computer Science."

    # ---------------------- Fees / Admission ----------------------
    elif "admission" in user_input:
        return "Admissions are based on online application and merit."

    elif "average fee" in user_input or "average fees" in user_input:
        return "The average fees for most courses are around ₹7,000 to ₹12,000 for 3 years."

    elif "fee" in user_input or "fees" in user_input:
        return "Fee details vary by course. Please contact the office."

    # ---------------------- Contact / Hostel / Location / Facilities ----------------------
    elif "contact" in user_input:
        return "You can contact us at +91-04255-251144 or email principalpalladam@gmail.com."

    elif "hostel" in user_input:
        return "Yes, we have separate hostel facilities available for boys and girls."

    elif "location" in user_input or "address" in user_input:
        return "Our college is located on Mangalam Road, Palladam."
    
    elif "college facilities" in user_input:
        return "Our college has Career Guidance, Placements and Women Cell."

    elif "timing" in user_input or "time" in user_input:
        return "College timing is 10:00 AM to 3:00 PM."

    # ---------------------- Library / Labs / Sports / Events ----------------------
    elif "scholarship" in user_input:
        return "We provide various scholarships primarily through government schemes."

    elif "library" in user_input:
        return "Our library has over 2475+ books and journals."

    elif "labs" in user_input or "laboratories" in user_input:
        return "We have well-equipped computer and science labs."

    elif "sports" in user_input:
        return "We offer facilities for cricket, football, volleyball, badminton, and athletics."

    elif "events" in user_input:
        return "We host annual cultural and sports events."

    # ---------------------- Accreditation / Full Name ----------------------
    elif "accreditation" in user_input:
        return "Our college is accredited by NAAC with a B+ grade."

    elif "fullform" in user_input or "full form" in user_input or "full name" in user_input:
        return "Puratchi Thalaivi Amma Government Arts and Science College."

    # ---------------------- Students / Placement / Canteen ----------------------
    elif "students" in user_input:
        return "Our college has a student strength of around 1500+ students."

    elif "placement" in user_input:
        return "Our college has a dedicated placement cell with a 90% track record in top companies like TCS, Infosys, and Wipro."

    elif "canteen" in user_input:
        return "The college canteen provides hygienic and affordable snacks and beverages."

    # ---------------------- Department / Stream / Faculties ----------------------
    elif "department" in user_input or "departments" in user_input:
        return ("Arts: Tamil, English\n"
                "Science: Maths, Computer Science, Chemistry, CDF\n"
                "Commerce: Commerce, CA, BI")

    elif "stream" in user_input or "streams" in user_input:
        return "The college has 3 streams: Arts, Science and Commerce."

    elif "faculties" in user_input or "profile" in user_input:
        return "Faculty details are available department wise. Please ask department name."
    
    elif "principal" in user_input:
         return "The principal of Puratchi Thalaivi Amma Government Arts and Science College, Palladam, is Dr. S. Manimegalai."

    # ---------------------- Staff by Department ----------------------
    elif "tamil" in user_input:
        return "Tamil Department Staff: S Mahalakshmi, P Jaisingh, Dr K Nagarathinam, Dr M Shanmuga Priya."

    elif "english" in user_input:
        return "English Department Staff: Dr R Krishnaveni, L Ram Prasad, Dr R Gobinath, Dr H Thippu Sulthan, Dr S Mukintha Priyadarsini."

    elif "maths" in user_input or "mathematics" in user_input:
        return "Mathematics Department Staff: P Anna Hycintha Helen, Dr V Rajendran, Dr S Maheswari."

    elif "computer science" in user_input or "cs" in user_input:
        return "Computer Science Department Staff: Dr N Vimala, Dr K Karthikeyan, A Balasubramanian, Dr T Jayalakshmi, Dr M Senthilkumar, V Prabha, Dr M Kiruthika."

    elif "chemistry" in user_input:
        return "Chemistry Department Staff: Dr M Jayandran, Dr V Selvaraju."

    elif "cdf" in user_input or "costume design" in user_input:
        return "Costume Design and Fashion Department Staff: S Ramadevi."

    elif "commerce" in user_input:
        return "Commerce Department Staff: Dr R Jeyachandran, Dr C Dharmaraj, Dr S David Soundararajan, Dr D P Krittihaa, Dr M S Kavitha, Dr V Sangeetha, Dr A Palanisamy, Dr T Thiruvaranga Selvi, Dr M Kaleeswari."

    elif "clp" in user_input or "computer literacy" in user_input:
        return "Computer Literacy Program Staff: T Keerthana, T Kowsalya Arthi, G Sangeetha."

    elif "club" in user_input or "clubs" in user_input:
        return "Anti-Drug Club, Cyber Club, Department Associations, Sports and Cultural Clubs are available."

    # ---------------------- Thanks ----------------------
    elif "thanks" in words or "thank you" in words:
        return "You're welcome! If you have any more questions, feel free to ask."

    # ---------------------- Greeting (Last) ----------------------
    elif "hai" in words or "hello" in words:
        return "Hello! How can I help you?"

    # ---------------------- Default ----------------------
    else:
        return "Sorry, I didn't understand that. Please ask about courses, fees, admission, contact, or timings."
