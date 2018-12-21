## Generated Story No1
* greet
    - utter_greet
* deny
    - utter_goodbye

## Generated Story No2
* greet
    - utter_greet
* goodbye
    - utter_goodbye

## Generated Story No3
* greet
    - utter_greet
* thanks
    - utter_thanks

## Generated Story No4
* unknown_intent
    - utter_default


## Generated Story No5
* greet
    - utter_greet
* request_search{"item": "取款"}
    - slot{"item": "取款"}
    - utter_ask_money
* ask_money{"money": "人民币"}
    - slot{"money": "人民币"}
    - utter_ask_place
* ask_place{"place": "本地"}
    - slot{"place": "本地"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No7
* greet
    - utter_greet
* request_search{"item": "取款", "money": "人民币"}
    - slot{"item": "取款"}
    - slot{"money": "人民币"}
    - utter_ask_place
* ask_place{"place": "本地"}
    - slot{"place": "本地"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No8
* greet
    - utter_greet
* request_search{"item": "取款", "place": "本地"}
    - slot{"item": "取款"}
    - slot{"place": "本地"}
    - utter_ask_money
* ask_money{"money": "人民币"}
    - slot{"money": "人民币"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No9
* greet
    - utter_greet
* request_search{"item": "取款", "money": "人民币", "place": "本地"}
    - slot{"item": "取款"}
    - slot{"money": "人民币"}
    - slot{"place": "本地"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye
	
## Generated Story No10
* greet
    - utter_greet
* ask_money{"money": "人民币", "place": "本地"}
    - slot{"money": "人民币"}
    - slot{"place": "本地"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye

## Generated Story No11
* greet
    - utter_greet
* ask_money{"money": "人民币"}
    - slot{"money": "人民币"}
    - utter_ask_place
* ask_place{"place": "本地"}
    - slot{"place": "本地"}
    - utter_confirm
* confirm
    - action_answer
    - utter_ask_morehelp
* deny
    - utter_goodbye
