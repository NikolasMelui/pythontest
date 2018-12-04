import json

save_data = []


def get_user_names(path):
    with open(path) as access_json:
        read_content = json.load(access_json)
        question_content = read_content['results']
        for question_data in question_content:
            question_replies = question_data['replies']
            for replies_data in question_replies:
                user_name = replies_data['user']['display_name']
                save_data.append(user_name)


get_user_names('./source-data.json')
print(save_data)
