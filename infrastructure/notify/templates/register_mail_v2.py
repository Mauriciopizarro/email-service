

def get_body(username):
    body = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome {username}!</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                background: linear-gradient(135deg, #6c5ce7, #fd79a8);
            }}
            h1 {{
                color: #ffffff;
                text-align: center;
            }}
            p {{
                color: #ffffff;
                text-align: center;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                color: #ffffff;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome {username}!</h1>
            <p>Your account has been successfully created.</p>
            <div class="footer">
                <p>Thank you,</p>
                <p>BlackJack team</p>
            </div>
        </div>
    </body>
    </html>
    """.format(username=username)

    return body
