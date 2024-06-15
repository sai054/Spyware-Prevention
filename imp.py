def button1_clicked():
    email = input("Enter your registered email: ")  # Prompt user to enter registered email
    if email in registered_emails:
        otp_window = tk.Toplevel(root)
        otp_window.title("Enter OTP")
        otp_window.geometry("300x200")
        otp_window.configure(bg="black")
        otp_label = tk.Label(otp_window, text="Enter Password for Camera Disable:", bg="white")
        otp_label.pack()
        otp_entry = tk.Entry(otp_window, show="*")
        otp_entry.pack()

        def ok_button():
            if otp_entry.get() == registered_emails[email]:
                delete_cmd = r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
                subprocess.run(delete_cmd, shell=True)
                add_cmd = r'REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_DWORD /d 0 /f'
                subprocess.run(add_cmd, shell=True)
                otp_window.destroy()
                success_label.config(text="Camera Disabled successfully")
            else:
                error_label.config(text="Incorrect OTP")
                otp_entry.delete(0, tk.END)

        ok_button = ttk.Button(otp_window, text="OK", command=ok_button, style="Custom.TButton")
        ok_button.pack(pady=(10, 0))

        error_label = tk.Label(otp_window, text="", font=("Arial", 12), bg="red", fg="black")
        error_label.pack()
    else:
        print("Email not registered.")

def button2_clicked():
    email = input("Enter your registered email: ")  # Prompt user to enter registered email
    if email in registered_emails:
        otp_window = tk.Toplevel(root)
        otp_window.title("Enter OTP")
        otp_window.geometry("300x200")
        otp_window.configure(bg="black")
        otp_label = tk.Label(otp_window, text="Enter Password for Camera Enable", bg="white")
        otp_label.pack()
        otp_entry = tk.Entry(otp_window, show="*")
        otp_entry.pack()

        def ok_button():
            if otp_entry.get() == registered_emails[email]:
                delete_cmd = r'REG DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
                subprocess.call(delete_cmd, shell=True)
                otp_window.destroy()
                success_label.config(text="Camera Enabled Successfully")
            else:
                error_label.config(text="Incorrect OTP")
                otp_entry.delete(0, tk.END)

        ok_button = ttk.Button(otp_window, text="OK", command=ok_button, style="Custom.TButton")
        ok_button.pack(pady=(10, 0))

        error_label = tk.Label(otp_window, text="", font=("Arial", 12), bg="red", fg="black")
        error_label.pack()
    else:
        print("Email not registered.")

def generate_password():
    # Generate a random password
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))  # Adjust the length as needed
    return password

def send_email(email, password):
    # Send email with generated password
    sender_email = 'helloguruotp@gmail.com'  # Your Gmail address
    sender_password = 'egmm ilav jsoa lgls'  # Your Gmail password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    message = f"Subject: Your Password\n\nYour password for the web camera security is: {password}.  \nBe cautious while using the password, don't share it with anyother inorder to maintain the privacy. \n \nBest Regards, \nTeam Helloguru OTP."
    server.sendmail(sender_email, email, message)
    server.quit()

def register_here():
    register_window = tk.Toplevel(root)
    register_window.title("Register Here")
    register_window.geometry("300x200")
    register_window.configure(bg="black")

    email_label = tk.Label(register_window, text="Enter Email:", bg="white")
    email_label.pack()

    email_entry = tk.Entry(register_window)
    email_entry.pack()

    status_label = tk.Label(register_window, text="", font=("Arial", 12), bg="black", fg="red")
    status_label.pack()

    def register_user():
        email = email_entry.get()
        if email:
            if '@' not in email or '.' not in email:
                status_label.config(text="Please enter a valid email address.")
            elif email in registered_emails:
                status_label.config(text="Email already registered. Please try another email.")
            else:
                password = generate_password()
                registered_emails[email] = password
                try:
                    send_email(email, password)
                    status_label.config(text="Registration successful. Check your email for the password.")
                except Exception as e:
                    print("Error sending email:", e)
                    status_label.config(text="Error sending email. Please try again later.")
                register_window.destroy()
        else:
            status_label.config(text="Please enter a valid email address.")

    register_button = ttk.Button(register_window, text="Register", command=register_user, style="Custom.TButton")
    register_button.pack(pady=(10, 0))

    status_label = tk.Label(register_window, text="", font=("Arial", 12), bg="black", fg="red")
    status_label.pack()

