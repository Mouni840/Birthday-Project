from fastapi import FastAPI, Request, Form, status
from fastapi.templating import Jinja2Templates
from models.users import UserModel
from fastapi.responses import RedirectResponse
app = FastAPI()
templates = Jinja2Templates(directory="html_templates")

if not os.path.exists("static"):
    os.makedirs("static")


userBirthDays = []


@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "birthdays": userBirthDays})


@app.post('/save_form_data')
def save_form_data(name: str = Form(...), year: str = Form(...), month: str = Form(...), day: str = Form(...)):
    # userBirthDays.append(UserModel(name=name, year=year, month=month, day=day))
    # print(userBirthDays)
    # print(name,year,month,day)

    data = UserModel(name=name, year=year, month=month, day=day)
    userBirthDays.append(data)
    print(data)
    print(userBirthDays)
    return RedirectResponse(url=app.url_path_for("root"), status_code=status.HTTP_303_SEE_OTHER)
