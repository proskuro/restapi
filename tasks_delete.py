import boto3
 
# 初期設定
db = boto3.resource('dynamodb')
tb = db.Table('tasks')

# delete処理
def delete_tasks(task_id):
    try:
        tb.delete_item(Key={'task_id': task_id})
        return {'statusCode': 200, 'message': 'success'}
    except:
        return {'statusCode': 400, 'message': 'bad request'}

# 初期実行         
def lambda_handler(event, context):
    if event['task_id'] != '':
        return delete_tasks(event['task_id'])
    else:
        return {'statusCode': 400, 'message': 'bad request'}