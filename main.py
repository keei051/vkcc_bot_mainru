
import os

BOT_TOKEN = "7348002301:AAH2AY0N6oFUWjK5OBn7epUWeD-63ZlSb-k"
VK_API_TOKEN = "c26551e5c26551e5c26551e564c1513cc2cc265c26551e5aa37c66a6a6d8f7092ca2102"

# пример исправления строки
link_list = [{"title": "Example", "short": "vk.cc/test"}]
stats = [{"views": 123}]
text = ""
text += "\n".join(f"🔗 {l['title']} ({l['short']}): {stats[i]['views']}" for i, l in enumerate(link_list))
print(text)
