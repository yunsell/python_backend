from flask import Blueprint, request, render_template

from app.module import dbModule

test = Blueprint('test', __name__, url_prefix='/')


@test.route('/', methods=['GET'])
def select():
    db_class = dbModule.Database()
    sql = "SELECT * FROM sentence"
    row = db_class.executeAll(sql)

    return render_template('/test/test.html', result=row)
#
#
# # INSERT 함수
# @test.route('/content', methods=['POST'])
# def content():
#     if request.method == 'POST':
#         db_class = dbModule.Database()
#         element = request.form['content']
#         print(element)
#         sql = "INSERT INTO testDB.testTable(test) \
#                     VALUES('{}')".format(element)
#         db_class.execute(sql)
#         db_class.commit()
#
#         return select()
#
# # UPDATE 함수
# @test.route('/update', methods=['POST'])
# def update():
#     db_class = dbModule.Database()
#     num = request.form['update']
#     print(num)
#     sql = "UPDATE testTable SET test='변경완료!' where idx = ('{}')".format(num)
#     db_class.execute(sql)
#     db_class.commit()
#
#     return select()
#
# # DELETE 함수
# @test.route('/delete', methods=['POST'])
# def delete():
#     db_class = dbModule.Database()
#     delnum = request.form['delete']
#     print(delnum)
#     sql = "DELETE FROM testTable WHERE idx = ('{}')".format(delnum)
#     db_class.execute(sql)
#     db_class.commit()
#
#     return select()