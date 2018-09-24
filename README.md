# Meistertask-Telegram-Bot
Hello World Project

When to update which file?


CASE 1: NEW MEMBER

update "a_telegram_username.json" on the droplet / virtual server for bots:  
structure:  
{"user1_forename user1_lastname": "telegram_username_user1", ...}


CASE 2: NEW TELEGRAM GROUP

update "b_dentacoin_projects_assigned_to_telegram_groups.json" on the droplet / virtual server for bots:  
structure:  
{"project1_name (name as in Meistertask)": "project1_shortcut (name as in "c_chat_id_telegram_groups.json")", ...}

update "c_chat_id_telegram_groups.json" on the droplet / virtual server for bots:  
structure:  
{"project1_shortcut (name as in "b_dentacoin_projects_assigned_to_telegram_groups.json")": "project1_chat_id_in_telegram", ...}
