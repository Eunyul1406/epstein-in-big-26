from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    my_name="Ngan"
    title="tuff prsn"
    contact_email="0855210179"
    # skill=['Clone Fb,','app thoi tiet', 'game san moi']
    
    my_skills = [
        {
            "skill_name": "Lập trình Scratch",
            "description": "Lập trình Scratch là một ngôn ngữ lập trình trực quan được thiết kế để giúp trẻ em và người mới bắt đầu học lập trình.",
            "percentage": 80,
            "certificate": 'docs/scratch.pdf',
            "step": 1

        },
        {
            "skill_name": "Lập trình Python cơ bản",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 70,
            "certificate": 'docs/python co ban.pdf',
            "step": 2
        },
        {
            "skill_name": "Lập trình Python nâng cao",
            "description": "Python là một ngôn ngữ lập trình phổ biến, dễ học và có ứng dụng rộng rãi trong nhiều lĩnh vực.",
            "percentage": 85,
            "certificate": 'docs/ngan_cert.pdf',
            "step": 3
        },
        {
            "skill_name": "Lập trình Web",
            "description": "Lập trình Web là quá trình tạo ra các trang web và ứng dụng web tương tác.",
            "percentage": 90,
            "certificate": 'docs/wsp.pdf',
            "step": 4
        }
    ]
    

    return render_template("index.html", name=my_name, bio=title, email=contact_email, my_skill=my_skills)

@app.route('/projects')
def projects():
    return 'This is not the projects page.'

@app.route('/about')
def about():
    return render_template("about.html")

if __name__=='__main__':
    app.run(debug=True)
