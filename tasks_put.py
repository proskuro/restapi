import boto3
import json

# 初期設定
db = boto3.resource('dynamodb')
tb = db.Table('tasks')

# put処理 
def put_tasks(req_json):
    try:
        # 更新処理
        tb.update_item(
            Key={'task_id': req_json['task_id']},
            UpdateExpression="SET title = :new_title, contents = :new_contents",
            ExpressionAttributeValues={
                ':new_title': req_json['title'],
                ':new_contents': req_json['contents']
            }
        )
        return {'statusCode': 200, 'message': 'success'}
    except:
        return {'statusCode': 400, 'message': 'bad request'}

# 初期実行
def lambda_handler(event, context):
    req_json = json.loads(event['body'])
    return put_tasks(req_json)
