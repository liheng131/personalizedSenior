# 请保存函数名为main,输入输出均为dict；最终结果会以json字符串方式返回，请勿直接返回不支持json.dumps的对象
def main(params: dict) -> dict:
    """
    该函数用于在紧急救援时，根据用户ID快速获取其紧急联系人信息和位置。

    参数:
    params (dict): 包含输入数据的字典。期望的键为 'userId'。
                   例如: {'userId': 'user_123'}

    返回值:
    dict: 一个包含紧急联系人姓名、电话和当前位置信息的字典。
          如果未找到用户，则返回一个包含错误信息的字典。
          例如: {'emergency_contact_name': '张三', 'emergency_contact_phone': '13812345678', 'current_location': '北京市朝阳区'}
    """

    # 模拟一个简单的数据库，存储紧急联系人信息
    # 在实际应用中，您可以连接到一个真正的数据库，如MySQL、PostgreSQL或MongoDB。
    # 为了快速演示，我们使用一个Python字典。
    mock_database = {
        'user_123': {
            'emergency_contact_name': '张三',
            'emergency_contact_phone': '13812345678',
            'current_location': '广东省深圳市宝安区',
        },
        'user_456': {
            'emergency_contact_name': '李四',
            'emergency_contact_phone': '13987654321',
            'current_location': '上海市浦东新区',
        },
        'user_789': {
            'emergency_contact_name': '王五',
            'emergency_contact_phone': '13711223344',
            'current_location': '广州市天河区',
        }
    }

    # 1. 从输入参数中获取用户ID
    user_id = params.get('userId')

    # 2. 检查用户ID是否有效
    if not user_id:
        user_id = 'user_123'
        # return {'error': '用户ID未提供。请在输入参数中包含 "userId"。'}

    # 3. 从模拟数据库中查找用户信息
    user_info = mock_database.get(user_id)

    # 4. 检查是否找到用户信息
    if user_info:
        # 如果找到，返回所需信息
        return {
            'emergency_contact_name': user_info['emergency_contact_name'],
            'emergency_contact_phone': user_info['emergency_contact_phone'],
            'current_location': user_info['current_location']
        }
    else:
        # 如果未找到，返回一个错误信息
        return {'error': f'未找到与用户ID {user_id} 匹配的信息。'}
