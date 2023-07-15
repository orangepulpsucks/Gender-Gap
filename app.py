import csv
from flask import Flask, request, render_template
import psycopg2, random

from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(
    "host=db dbname=postgres user=postgres password=postgres",
    cursor_factory=RealDictCursor)
app = Flask(__name__)

# HOME -> 1
@app.route('/')
def render_sets1():
    Age = request.args.get("Age", "")
    EdLevel = request.args.get("Edlevel", "")
    Gender = request.args.get("Gender", "")
    MainBranch = request.args.get("MainBranch", "")
    YearsCode = request.args.get("YearsCode", "")
    Country = request.args.get("Country", "")
    HaveWorkedWith = request.args.get("HaveWorkedWith", "")
    ComputerSkills = request.args.get("ComputerSkills", "")
    
    sort_by = request.args.get("sort_by", "series_title")
    sort_dir = request.args.get("sort_dir", "asc")
    limit = request.args.get("limit", 1000, type=int)

#gender_d, edlevel_d, mainbranch_d, yearscode, computerskills,haveworkedwith, country
    from_where_clause1 = """
        from theme
        where %(Gender)s is null or gender ilike %(Gender)s
        and ( %(EdLevel)s is null or edlevel = %(EdLevel)s )
        and ( %(MainBranch)s is null or mainbranch = %(MainBranch)s )
        and ( %(YearsCode)s is null or yearscode ilike %(YearsCode)s )
        and ( %(ComputerSkills)s is null or computerskills = %(ComputerSkills)s )
        and ( %(HaveWorkedWith)s is null or haveworkedwith ilike %(HaveWorkedWith)s )
        and ( %(Country)s is null or country ilike %(Country)s )
    """

    params1 = {
        "Gender": f"%{Gender}%",
        "EdLevel": f"%{EdLevel}%",
        "MainBranch": f"%{MainBranch}",
        "YearsCode": int(YearsCode) if YearsCode and YearsCode.isdigit() else 0
        if YearsCode and not YearsCode.isdigit() else None,
        "ComputerSkills": int(ComputerSkills) if ComputerSkills and ComputerSkills.isdigit() else 0
        if ComputerSkills and not ComputerSkills.isdigit() else None,
        "HaveWorkedWith": f"%{HaveWorkedWith}",
        "Country": f"%{Country}",

        "sort_by": sort_by,
        "sort_dir" : sort_dir,
        "limit" : limit
}

    def get_sort_dir1(col):
        if col== sort_by:
            return "desc" if sort_dir == "asc" else "asc"
        else:
            return "asc"
   #gender_d, edlevel_d, mainbranch_d, yearscode, computerskills,haveworkedwith, country
     
    with conn.cursor() as cur:
        cur.execute(f"""gender, edlevel, mainbranch, yearscode, computerskills, haveworkedwith, country
                        {from_where_clause1} 
                        order by {sort_by} {sort_dir} 
                        limit %(limit)s 
                    """,
                    params1)
        results1 = list(cur.fetchall())  


    return render_template("home.html",
                           params1=request.args
                           )    

@app.route("/about")
def render_sets2():
    return render_template("about.html")
   
