messages = []
user_messages = {}
n = int(input("Enter the number of messages: "))
for i in range(n):
    msg = input(f"Enter message {i+1}: ")
    messages.append(msg)

    if ":" in msg:
        name, text = msg.split(":", 1)
        name = name.strip()
        text = text.strip()
        if name not in user_messages:
            user_messages[name] = []
        user_messages[name].append(text)
while True:
    print("Menu Options")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Average words per message")
    print("5. Longest message")
    print("6. Most active user")
    print("7. Message count for user")
    print("8. Most frequent word by user")
    print("9. First and last message by user")
    print("10. Check user presence")
    print("11. Common repeated words")
    print("13. Longest average message user")
    print("14. Messages mentioning user")
    print("15. Remove duplicate messages")
    print("16. Sort messages A-Z")
    print("17. Extract questions")
    print("18. Reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        print("Total messages:", len(messages))

    elif ch == "2":
        users = set()
        for m in messages:
            if ":" in m:
                name = m.split(":")[0].strip()
                users.add(name)
        print("Unique users in the chat:", users)

    elif ch == "3":
        total = 0
        for m in messages:
            parts = m.split(":", 1)
            if len(parts) == 2:
                words = parts[1].strip().split()
                total += len(words)
        print("Total words in the chat:", total)

    elif ch == "4":
        total = 0
        for m in messages:
            parts = m.split(":", 1)
            if len(parts) == 2:
                words = parts[1].strip().split()
                total += len(words)
        avg = total / len(messages) if messages else 0
        print("Average words per message:", round(avg, 2))

    elif ch == "5":
        max_msg = ""
        for m in messages:
            if len(m) > len(max_msg):
                max_msg = m
        print("Longest message:", max_msg)

    elif ch == "6":
        max_count = 0
        top_user = ""
        for u in user_messages:
            if len(user_messages[u]) > max_count:
                max_count = len(user_messages[u])
                top_user = u
        print(f"Most active user: {top_user} ({max_count} messages)")

    elif ch == "7":
        u = input("Enter user name: ")
        if u in user_messages:
            print(f"Messages sent by {u}: {len(user_messages[u])}")
        else:
            print(f"User '{u}' not found.")

    elif ch == "8":
        u = input("Enter user name: ")
        if u in user_messages:
            word_count = {}
            for msg in user_messages[u]:
                for word in msg.lower().split():
                    word_count[word] = word_count.get(word, 0) + 1
            if word_count:
                most = max(word_count, key=word_count.get)
                print(f"Most frequent word used by {u}: \"{most}\"")
            else:
                print("No words found.")
        else:
            print("User not found.")

    elif ch == "9":
        u = input("Enter user name: ")
        first = ""
        last = ""
        for m in messages:
            if m.startswith(u + ":"):
                if first == "":
                    first = m
                last = m
        if first:
            print("First message by", u + ":", first)
            print("Last message by", u + ":", last)
        else:
            print("No messages from that user.")

    elif ch == "10":
        u = input("Enter user to check: ")
        if u in user_messages:
            print(f"User '{u}' is present in the chat.")
        else:
            print(f"User '{u}' not found in the chat.")

    elif ch == "11":
        word_count = {}
        for m in messages:
            if ":" in m:
                text = m.split(":", 1)[1].strip()
                for word in text.lower().split():
                    word_count[word] = word_count.get(word, 0) + 1
        repeated = set()
        for word in word_count:
            if word_count[word] > 1:
                repeated.add(word)
        print("Common repeated words:", repeated)

    elif ch  == "13":
        max_avg = 0
        max_user = ""
        for u in user_messages:
            total_words = 0
            for msg in user_messages[u]:
                total_words += len(msg.split())
            avg = total_words / len(user_messages[u])
            if avg > max_avg:
                max_avg = avg
                max_user = u
        print(f"User with longest average message: {max_user} (avg {round(max_avg, 2)} words)")

    elif ch  == "14":
        name = input("Enter name to check mentions: ").lower()
        count = 0
        for m in messages:
            if name in m.lower().split(":", 1)[1]:
                count += 1
        print(f"Messages mentioning '{name}': {count}")

    elif ch  == "15":
        unique = list(set(messages))
        print("Unique messages count:", len(unique))
        for msg in unique:
            print(msg)

    elif ch  == "16":
        sorted_msgs = sorted(messages)
        for msg in sorted_msgs:
            print(msg)

    elif ch == "17":
        print("Questions in chat:")
        for msg in messages:
            if "?" in msg:
                print(msg)

    elif ch  == "18":
        u1 = input("Enter first user: ").strip()
        u2 = input("Enter second user: ").strip()
        count = 0
        for i in range(1, len(messages)):
            if messages[i-1].startswith(u1 + ":") and messages[i].startswith(u2 + ":"):
                count += 1
        print(f"Reply ratio from {u2} to {u1}: {count} replies")

    elif ch  == "19":
        deleted = 0
        for m in messages:
            if "This message was deleted" in m:
                deleted += 1
        print(f"Deleted messages found: {deleted}")

    elif ch == "0":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
