
def get_body_mail_verification_code(code):
    body = """
    <html>
      <head>
        <meta charset="UTF-8">
        <title>Welcome</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
          body {{
            font-family: Arial, sans-serif;
            font-size: 16px;
            line-height: 1.5;
            color: #444444;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
          }}
          header {{
            background-color: #0088cc;
            color: #ffffff;
            padding: 20px;
            text-align: center;
          }}
          footer {{
            background-color: #0088cc;
            color: #ffffff;
            padding: 20px;
          }}
          .content {{
            background-color: #ffffff;
            padding: 20px;
          }}
          .button {{
            display: inline-block;
            background-color: #0088cc;
            color: #ffffff;
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            margin-top: 20px;
          }}
        </style>
      </head>
      <body>
        <header>
          <h1>Hi, your verification code is {code}</h1>
        </header>
        <div class="content">
          <p>Enter this code in the app to reset your password.</p>
          <p>All the best</p>
          <p>App team</p>
        </div>
      </body>
    </html>
    """.format(code=code)

    return body