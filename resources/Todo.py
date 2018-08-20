from flask import request, jsonify
from flask_restful import Resource
from Model import db, Todo, TodoSchema

todos_schema = TodoSchema(many=True)
todo_schema = TodoSchema()

class TodoResource(Resource):
    def get(self):
        todos = Todo.query.all()
        todos = todos_schema.dump(todos).data
        return {'success': todos}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
               return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        # errors = todo_schema.load(json_data)
        # if errors:
        #     return errors, 422
        todo = Todo(    
            title=json_data['title'],
            status=json_data['status'],
            )
        print (todo)
        db.session.add(todo)
        db.session.commit()
        data = []
        for item in Todo.query.all():
            data.append({'title': item.title, 'status':item.status, 'id':item.id})
        return jsonify({'success': data})

    def put(self):
        data = request.get_json(force=True)
        if not data:
               return {'message': 'No input data provided'}, 400
        todo = Todo.query.filter_by(id=data['id']).first()
        if not todo:
            return {'message': 'Todo does not exist'}, 400
        todo.title = data['title']
        todo.status = data['status']
        db.session.commit()

        result = ({'title': todo.title, 'status':todo.status, 'id':todo.id})
        return jsonify({'success': result})

    def delete(self):
        data = request.get_json(force=True)
        if not data:
               return {'message': 'No input data provided'}, 400
        todo = Todo.query.filter_by(id=data['id']).delete()
        db.session.commit()

        return jsonify({'success': "Successfully Deleted."})