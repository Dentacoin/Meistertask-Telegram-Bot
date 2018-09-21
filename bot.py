import requests
import json
from datetime import datetime
import urllib



### MEISTERTASK-API

#BASIC STUFF FOR AUTHORIZATION

def token(filename):
    with open(filename, "r") as file:
        token_temp = str(file.read()).strip('\n')
        return token_temp

headers = {"Authorization":"Bearer " + token("meistertask_token.txt")}

#REQUESTS TO THE ENDPOINTS:
request_all_persons = json.loads(requests.get("https://www.meistertask.com/api/persons",headers=headers).text)
request_all_active_projects = json.loads(requests.get("https://www.meistertask.com/api/projects?status=active",headers=headers).text)
request_all_sections = json.loads(requests.get("https://www.meistertask.com/api/sections?",headers=headers).text)
request_all_tasks = json.loads(requests.get("https://www.meistertask.com/api/tasks?",headers=headers).text)


#REQUESTS PRETTIER TO READ
request_all_persons_pretty = json.dumps(request_all_persons, indent=4)
request_all_active_projects_pretty = json.dumps(request_all_active_projects, indent=4)
request_all_sections_pretty = json.dumps(request_all_sections, indent=4)
request_all_tasks_pretty = json.dumps(request_all_tasks, indent=4)


#DICTIONARIES OF PERSONS, PROJECTS, SECTIONS, TASKS (COMMENTS)
person_id_dict = {}
for i in range(0, len(request_all_persons)):
    person_id_dict[request_all_persons[i]['id']] = str(request_all_persons[i]['firstname'] + " " + request_all_persons[i]['lastname'])

project_id_list = []
for i in range(0, len(request_all_active_projects)):
    project_id_list.append(request_all_active_projects[i]['id'])

project_id_dict = {}
for i in range(0, len(request_all_active_projects)):
    project_id_dict[request_all_active_projects[i]['id']] = request_all_active_projects[i]['name']

section_id_list = []
for i in range(0, len(request_all_sections)):
    section_id_list.append(request_all_sections[i]['id'])

section_id_dict = {}
for i in range(0, len(request_all_sections)):
    section_id_dict[request_all_sections[i]['id']] = request_all_sections[i]['name']

section_id_project_name_dict = {}
for i in range(0, len(request_all_sections)):
    section_id_project_name_dict[request_all_sections[i]['id']] = project_id_dict[request_all_sections[i]['project_id']]

section_id_project_id_dict = {}
for i in range(0, len(request_all_sections)):
    section_id_project_id_dict[request_all_sections[i]['id']] = request_all_sections[i]['project_id']


task_id_dict_all = {}
for i in range (0, len(request_all_tasks)):
    task_id_dict_all[request_all_tasks[i]['id']] = request_all_tasks[i]

task_id_project_id_dict = {}
for i in range(0, len(request_all_tasks)):
    task_id_project_id_dict[request_all_tasks[i]['id']] = section_id_project_id_dict[request_all_tasks[i]['section_id']]

#ZEIT FORMATIERUNG
def formatted_date(Date_and_Time_unformatted):
    if Date_and_Time_unformatted == None:
        return
    else:
        Date_and_Time = datetime.strptime(Date_and_Time_unformatted, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted = str(format(Date_and_Time.day, "02")) + "." + str(format(Date_and_Time.month, "02")) + "." + str(Date_and_Time.year)
        return formatted




# ### TELEGRAM-BOT
#
# ###TEMP
# request_all_tasks_0 = [{'id': 29255251, 'token': 'gQnSS2YU', 'name': 'Modify the ban rules', 'notes': '', 'notes_html': 'alte notes html', 'status': 1, 'status_updated_at': '2018-07-02T13:28:31.000000Z', 'section_id': 9018907, 'sequence': 1.0, 'assigned_to_id': 32126941, 'due': '2018-07-06T09:00:00.000000Z', 'created_at': '2018-07-02T13:17:26.748509Z', 'updated_at': '2018-07-02T13:30:49.584830Z'}, {'id': 29260355, 'token': 'm1fAhQHJ', 'name': 'Copy answers from another Q', 'notes': 'Enable following features:\n- Save answers added manually as predefined answers for future use.\n- Copy answers from another question.', 'notes_html': '<p>Enable following features:</p>\n\n<ul>\n<li>Save answers added manually as predefined answers for future use.</li>\n<li>Copy answers from another question.</li>\n</ul>\n', 'status': 8, 'status_updated_at': '2018-07-17T14:03:47.022978Z', 'section_id': 9018907, 'sequence': 2.0, 'assigned_to_id': None, 'due': None, 'created_at': '2018-07-02T14:07:47.035671Z', 'updated_at': '2018-07-17T14:03:47.023263Z'}]
# request_all_tasks_1 = [{'id': 29255251, 'token': 'gQnSS2YU', 'name': 'Modify the ban rules (NEU)', 'notes': 'Neue_Notes ohne html', 'notes_html': '<p>This is html-text</p>', 'status': 2, 'status_updated_at': '2018-07-02T13:28:31.000000Z', 'section_id': 9018907, 'sequence': 1.0, 'assigned_to_id': 32512902, 'due': '2018-07-05T09:00:00.000000Z', 'created_at': '2018-07-02T13:17:26.748509Z', 'updated_at': '2018-07-02T13:30:49.584830Z'}, {'id': 30376008, 'token': '4z0ncrJE', 'name': 'Clarification Meeting with Alex', 'notes': 'Friday, July 27th', 'notes_html': '<p>Friday, July 27th</p>\n', 'status': 2, 'status_updated_at': '2018-08-14T07:09:11.989010Z', 'section_id': 9282074, 'sequence': 0.0, 'assigned_to_id': 32512902, 'due': '2018-07-27T09:00:00.000000Z', 'created_at': '2018-07-24T07:12:55.373106Z', 'updated_at': '2018-08-14T07:09:14.501628Z'}, {'id': 29260355, 'token': 'm1fAhQHJ', 'name': 'Copy answers from another Q', 'notes': 'Enable following features:\n- Save answers added manually as predefined answers for future use.\n- Copy answers from another question.', 'notes_html': '<p>Enable following features:</p>\n\n<ul>\n<li>Save answers added manually as predefined answers for future use.</li>\n<li>Copy answers from another question.</li>\n</ul>\n', 'status': 8, 'status_updated_at': '2018-07-17T14:03:47.022978Z', 'section_id': 9018907, 'sequence': 2.0, 'assigned_to_id': None, 'due': None, 'created_at': '2018-07-02T14:07:47.035671Z', 'updated_at': '2018-07-17T14:03:47.023263Z'}]
# tasks0 = request_all_tasks_0
# tasks1 = request_all_tasks_1
# ####TEMP

# # TEMP für ersten Durchlauf
# tasks0 = request_all_tasks






# Zeitpunkt 0 (Stand vor 1 Minute) -> aus json temp_snapshot.json laden
with open("temp_snapshot.json", 'r') as json_file:
   tasks0 = json.load(json_file)


# Zeitpunkt 1 (nachher) -> aktuelle API-Abfrage
tasks1 = request_all_tasks


################################## NACHRICHTEN VERSCHICKEN
################################## FALL 1: NEUE TASK WIRD ERSTELLTlsd

# VORBEREITUNG
#Liste der bot messages, die gesendet werden:
bot_message_new_task = []
#Zuordnung bot message - project id (damit der Bot weiß in welche Gruppe er welche Message posten soll
bot_message_new_task_dict = {}
# Aus telegram_usernames_outside (aus a_telegram_usernames.json) wird ein dictionary nur mit Zahlen (person_id: telegram_username)
with open("a_telegram_usernames.json", 'r') as telegram_usernames_file:
   telegram_usernames = json.load(telegram_usernames_file)


#Falls dazugekommen, neue Tasks (zum Anhängen an tasks0 -> Nur dann können die Daten im nächsten Schritt auf Veränderungen geprüft werden)
new_tasks_to_append = []

#Link auf die Task (für bot message):
def task_link_def(token):
    link = "https://www.meistertask.com/app/task/" + str(token) + "/"
    return link

status_dict = {1: "open", 2: "completed", 8: "trashed", 18: "completed & archived"}


# Test: Besitzen beide json-Dateien die gleiche Länge (=Anzahl von Dictionaries = Anzahl an Tasks)
if len(tasks0).__eq__(len(tasks1)) == False:

    #Falls nein, dann
    #Liste mit IDs aller Tasks zum Zeitunkt 0 (früherer Zeitpunkt)
    IDs_tasks_0 = []
    for i in range(0, len(tasks0)):
        IDs_tasks_0.append(tasks0[i]['id'])

    # Liste mit IDs aller Tasks zum Zeitunkt 1 (späterer Zeitpunkt)
    IDs_tasks_1 = []
    for j in range(0, len(tasks1)):
        IDs_tasks_1.append(tasks1[j]['id'])

    #Prüfe welche ID ist neu dazugekommen (neue ID = id_neue_task)
    for k in range(0, len(IDs_tasks_1)):
        if IDs_tasks_1[k] not in IDs_tasks_0:
            id_neue_task = IDs_tasks_1[k]
            new_tasks_to_append.append(task_id_dict_all[id_neue_task])
            task_link = task_link_def(task_id_dict_all[id_neue_task]['token'])

            hyperlink_format = '<a href="{link}">{text}</a>'
            task_name = "<b>{}</b>".format(str(hyperlink_format.format(link=task_link, text=str(task_id_dict_all[id_neue_task]['name']))))
            section_name = "<b>{}</b>".format(str(section_id_dict[task_id_dict_all[id_neue_task]['section_id']]))
            project_name = "<b>{}</b>".format(str(section_id_project_name_dict[task_id_dict_all[id_neue_task]['section_id']]))
            person_name = "<b>{}</b>(@{})".format(str(person_id_dict[task_id_dict_all[id_neue_task]['assigned_to_id']]),str(telegram_usernames[person_id_dict[task_id_dict_all[id_neue_task]['assigned_to_id']]]))
            formatted_due_date = "<b>{}</b>".format(formatted_date(task_id_dict_all[id_neue_task]['due']))

            ##Generiere eine Message, dass eine neue Task erstellt wurde abhängig von den Infos zur Task (ist assigned_to_id, notes oder due bereits vorhanden? Falls ja muss das in die Message)

            #wenn notes nicht None, dann Füge Notes in Klammern hinter Taskname und Link hinzu
            if task_id_dict_all[id_neue_task]['notes'] != None:
                task_notes = "(" + str(task_id_dict_all[id_neue_task]['notes']) + ")"
            else:
                task_notes = ""

            #wenn assigned_to_id nicht None, dann Füge Satz mit Person hinzu.
            if task_id_dict_all[id_neue_task]['assigned_to_id'] != None:
                assigned = " It is assigned to " + person_name + "."
            else:
                assigned = ""

            # wenn due nicht None, dann füge Satz mit due date hinzu (the due date is xx.xx.xxxx)
            if task_id_dict_all[id_neue_task]['due'] != None:
                due_date = " The due date is " + formatted_due_date + "."
            else:
                due_date = ""

            bot_message_new_task_temp = "The task " + task_name + " " + task_notes + " was created in section '" + section_name + "' of project '" + project_name + "'." + assigned + due_date
            bot_message_new_task.append(bot_message_new_task_temp)
            bot_message_new_task_dict[bot_message_new_task_temp] = task_id_project_id_dict[id_neue_task]




# wenn neue Task dazugekommen ist, füge diese neue Task den alten Daten hinzu. Nach dem Hinzufügen müssen die Daten dann noch sortiert werden, damit die Vergleichsfunktion korrekt funktioniert.
tasks0temp = tasks0
tasks0 = tasks0temp+new_tasks_to_append

# Daten nach ID sortieren:
tasks0s = sorted(tasks0, key=lambda k: k['id'])
tasks1s = sorted(tasks1, key=lambda k: k['id'])


################################## FALL 2: TASK WIRD GEÄNDERT

task_keys = []
for key in tasks0s[0]:
    task_keys.append(key)

#Liste der bot messages, die gesendet werden:
bot_message_task_changed = []
#Zuordnung bot message - project id (damit der Bot weiß in welche Gruppe er welche Message posten soll
bot_message_task_changed_dict = {}

for i in range(0, len(tasks0s)):
    t0 = tasks0s[i]
    t1 = tasks1s[i]
    for j in range(0, len(task_keys)):
        task0 = tasks0s[i][task_keys[j]]
        task1 = tasks1s[i][task_keys[j]]

        if task0.__eq__(task1) == False:

            #VORBEREITUNG/VEREINFACHUNG:
            key_which_has_changed = task_keys[j]

            # Link auf die Task (für bot message):
            task_link = task_link_def(t1['token'])
            task_name_new = "<b>{}</b>".format(str(hyperlink_format.format(link=task_link, text="'" + str(t1["name"]) + "'")))
            notes_new = "<b>{}</b>".format(str(t1["notes_html"]))
            status_new = "<b>{}</b>".format(str(status_dict[t1["status"]]))
            section_name_new = "<b>{}</b>".format(str(section_id_dict[t1['section_id']]))
            section_name_old = str(section_id_dict[t0['section_id']])
            project_name = "<b>{}</b>".format(str(section_id_project_name_dict[t1['section_id']]))
            due_date_new = "<b>{}</b>".format(str(formatted_date(t1["due"])))
            person_assigned_new = "<b>{}</b>(@{})".format(str(person_id_dict[t1["assigned_to_id"]]),str(telegram_usernames[person_id_dict[task_id_dict_all[id_neue_task]['assigned_to_id']]]))



            #Fall 1: Der Name wurde geändert
            if key_which_has_changed == 'name':
                message_name_changed = "The name of the task " + str(t0["name"]) + " was changed to " + task_name_new + " (section " + section_name_new + " at project " + project_name + ")"
                bot_message_task_changed.append(message_name_changed)
                bot_message_task_changed_dict[message_name_changed] = task_id_project_id_dict[t0["id"]]

            #Fall 2: Die Notizen (notes) wurden geändert
            if key_which_has_changed == 'notes_html':
                message_notes_changed = "The notes of the task " + task_name_new + " have been changed to " + notes_new + " (section " + section_name_new + " at project " + project_name + ")"
                bot_message_task_changed.append(message_notes_changed)
                bot_message_task_changed_dict[message_notes_changed] = task_id_project_id_dict[t0["id"]]

            #Fall 3: Der Status wurde geändert
            if key_which_has_changed == 'status':
                message_status_changed = "The status of the task " + task_name_new + " has been changed to " + status_new + " (section " + section_name_new + " at project " + project_name + ")"
                bot_message_task_changed.append(message_status_changed)
                bot_message_task_changed_dict[message_status_changed] = task_id_project_id_dict[t0["id"]]

            #Fall 4: Das Fälligkeitsdatum (due) wurde geändert
            if key_which_has_changed == 'due':
                message_duedate_changed = "The due date of the task " + task_name_new + " has been changed to " + due_date_new + " (section " + section_name_new + " at project " + project_name + ")"
                bot_message_task_changed.append(message_duedate_changed)
                bot_message_task_changed_dict[message_duedate_changed] = task_id_project_id_dict[t0["id"]]

            #Fall 5: Die zuständige Person (assigned_to_id) wurde geändert (Eine Task kann nur einer Person zugeordnet werden)
            if key_which_has_changed == 'assigned_to_id':
                message_assigned_to_changed = "The task " + task_name_new + " is now assigned to " + person_assigned_new + " (section " + section_name_new + " at project " + project_name + ")"
                bot_message_task_changed.append(message_assigned_to_changed)
                bot_message_task_changed_dict[message_assigned_to_changed] = task_id_project_id_dict[t0["id"]]

            #Fall 6: Die Task wurde in eine andere Section verschoben (section_id hat sich geändert)
            if key_which_has_changed == 'section_id':
                message_section_changed = "The task '" + task_name_new + "' has been moved to section " + section_name_new + " from " + section_name_old + " at project " + project_name
                bot_message_task_changed.append(message_section_changed)
                bot_message_task_changed_dict[message_section_changed] = task_id_project_id_dict[t0["id"]]


### BOT MESSAGES GENERIEREN (ABHÄNGIG VON PROJEKT)


URL = "https://api.telegram.org/bot{}/".format(token("telegram_token.txt"))

# hier geklaut: https://www.codementor.io/garethdwyer/building-a-telegram-bot-using-python-part-1-goi5fncay

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode={}".format(text, chat_id, "HTML")
    get_url(url)


#CHAT-IDs der einzelnen Telegram Gruppen
with open("c_chat_id_telegram_groups.json", 'r') as chat_id_file:
    chat_id = json.load(chat_id_file)

#Aus which_group_text (aus b_dentacoin_projects_assigned_to_telegram_groups.json) wird dictionary "which_groups" nur mit Zahlen (project_id: chat_id_telegram)
with open("b_dentacoin_projects_assigned_to_telegram_groups.json", 'r') as which_group_text_file:
    which_group_text = json.load(which_group_text_file)
which_group = {}
for i in range (0, len(project_id_list)):
    which_group[project_id_list[i]] = chat_id[which_group_text[project_id_dict[project_id_list[i]]]]


###AUSGABE DER BOT-MESSAGES FÜR BYOBU
print(bot_message_new_task)
print(bot_message_task_changed)


##########
## Chats werden abgeschickt (NEUE TASK)
for i in range (0, len(bot_message_new_task)):
    send_message(str(bot_message_new_task[i]), which_group[bot_message_new_task_dict[bot_message_new_task[i]]])

## Chats werden abgeschickt (VERÄNDERTE TASK)

for i in range (0, len(bot_message_task_changed)):
    send_message(str(bot_message_task_changed[i]), which_group[bot_message_task_changed_dict[bot_message_task_changed[i]]])
###########



## tasks1 in json exportieren und alte Daten überschreiben

with open('temp_snapshot.json', 'w') as outfile:
    json.dump(tasks1, outfile)
