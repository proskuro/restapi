import boto3

# 初期設定 
db = boto3.resource('dynamodb')
tb = db.Table('tasks')

# get処理(全て)
def get_tasks():
    try:
        #raise ValueError("error!")
        response = tb.scan()
        return {'statusCode': 200, 'message': 'success', 'response':response['Items']}
    except:
        return {'statusCode': 400, 'message': 'bad request'}

# get処理(個別)
def get_task(task_id):
    try:
        response = tb.get_item(Key={'task_id': task_id})
        return {'statusCode': 200, 'message': 'success', 'response':response['Item']}
    except:
        return {'statusCode': 400, 'message': 'bad request'}

# 初期実行
def lambda_handler(event, context):
    if event['task_id'] == '':
        return get_tasks()
    else:
        return get_task(event['task_id'])