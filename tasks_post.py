import boto3
import json

# 初期設定
db = boto3.resource('dynamodb')
tb = db.Table('tasks')

# post処理 
def post_tasks(req_json):
    try:
        # 新規登録
        tb.put_item(
            Item={
                'task_id': req_json['task_id'],
                'title': req_json['title'],
                'contents': req_json['contents']
            }
        )
        return {'statusCode': 200, 'message': 'success'}
    except:
        return {'statusCode': 400, 'message': 'bad request'}

# 初期実行
def lambda_handler(event, context):
    req_json = json.loads(event['body'])
    return post_tasks(req_json)