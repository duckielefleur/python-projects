print("""\
______________ ______________   ________._____________.____     
\__    ___/   |   \_   _____/  /  _____/|   \______   \    |    
  |    | /    ~    \    __)_  /   \  ___|   ||       _/    |    
  |    | \    Y    /        \ \    \_\  \   ||    |   \    |___ 
  |____|  \___|_  /_______  /  \______  /___||____|_  /_______ \
                                                  
         ⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢠⠣⠐⠀ ⭕ ￼ ⠀⠀⢪⢺⣪⢣⠀⡀ ⭕     . 
⠀⠀⠀⠀⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡⠀⠀⠀ 
⠀⠀⠀⠀⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂
                    """)
name = input("\nI was headed out of the library but the security guard stopped me. He asked me to sign out by filling my name on a sheet before i left. So I did... \nWhat's my name? ")
print("\nIt was around 23:20 that night... ")
step = input("\nI was dragging myself home exhausted after a tiring night-study session on campus. \nContinue walking: Type \'CONTINUE\' to keep moving: ").lower()
print("\nI was dragging myself home exhausted after a tiring night-study session on campus.")
print("\n \nBut there was no one on the street, which I thought was strange. \nI usually see a lot of people, even at night since my apartment complex is pretty big and busy.")
scared = input ("\n \nAnyways, feeling scared, I thought about looking down on the ground while walking home. \nType \'LOOK DOWN\' to look down or \'CONTINUE\'' to proceed: ").lower()
if scared == "look down":
      print("\n \nSuddenly, a shadow stretching towards me caught my eyes... although there wasn't anyone around me")
      look = input ("Look up... \n Type \'LOOK\' to see who it was: ").lower()
      if look == "look":
        looked = input ("\n \nI saw a woman walking in front of me. But she looked a little strange. \nI could see she looked crippled. She was limping and struggling to walk in front of me.\nContinue walking: Type \'CONTINUE\'to keep moving: ").lower()
      if looked == "continue":
        print("\nSince she was walking very slow, I soon caught up with her.")
        better1 = input ("\nI got closer and saw her better.. \nDescribe what I saw: Type \'DESCRIBE\'to explain what you see: ").lower()
        if better1 == "describe":
          print("\n\nShe was wearing dirty pink pajamas and looked as if all the joints in her body had been twisted. \nWorse, her hair was a mess and stickingout everywhere...")
          help = input ("\n\"HELP... "+name+"'\' she exclaimed. \nHow did she know my name? \n\nType \'STOP\' to stop and ask or \'CONTINUE\' to proceed: ").lower()
          if help == "stop":
            print("\n\nIt seemed so weird so I stopped walking...")
            she_calls1 = input ("\n\"HEEELP!!!\" she exclaimed again. Do I go to her or go the other way?\nType \'FIND OUT\' to approach her or \'TURN AROUND\' to go the other way: ").lower()
            if she_calls1 == "turn around":
              print("\n\nas I turned around, i felt her creep up behind me...\ncloser...\n\ncloser...\n\n\n and she put her hand on my shoulder... \nShe then screamed \"WHERE IS MY BABY?!?!?\"")
              my_thoughts1 = input("\nType \'ANSWER\' to point to where the baby is or \'SILENT\' to give no response: ").lower()
              if my_thoughts1 == "answer":
                print("\nI answered pointing as far as I could. \"Over there\" I said terrified")
                print("\nI wanted to see her get away from me. As far as possible... \nThen, she limped towards where I had pointed... \n and i couldn't see her anymore")
                go_home1 = input ("\nAs soon as she had disappeared from my line of sight...\nI had to go to a...\nany place where people are around! \n\nand at that moment...\n \n\"SHE IS NOT HERE!\" \nI heard her screaming far away. \"Should I run???\", I thought to myself... \nType \'RUN\' to get tf out of there!!! or \'STAY CALM\' to avoid giving her attention: ").lower()
                if go_home1 == "run":
                  print("\n I began to run as fast as I could but then...\n\nShe jumped on my back. We began to struggle but her strength was something I never experienced. \nBefore I could even begin to process what was happen, I had been stabbed... bleeding out on the floor... my consciousness began to fade...")
                  print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
                elif go_home1 == "stay calm":
                  print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                  print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
            elif she_calls1 == "find out":
              print("\nShe screamed \"WHERE IS MY BABY?!?!?\"")
              print("\nI reached out to ask this crazy woman how she knew my name... \nI put my hands on her shoulder and before i could react, I felt a blade, as cold as ice, plunged into my chest...\n\nI had been stabbed... bleeding out on the floor... my consciousness began to fade...")
              print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
          elif help == "continue":
            print("\n\"I felt like i shouldn't get any closer to her nor did I have the guts to pass her by\", I thought to myself")
            print("\nYou know, when people say that if you are really in shock, you can't even scream...\n That was right...\n I froze there, not being able to move at all. Paralysed by fear...")
            print("\nShe reached out to me and put her hand on my shoulder... \nShe then screamed \"WHERE IS MY BABY?!?!?\"")
            my_thoughts2 = input("\nType \'answer\' to point to where the baby is or \'silent\' to give no response ").lower()
            if my_thoughts2 == "answer":
              print("\nI answered pointing as far as I could. \"Over there\" I said terrified")
              print("\nI wanted to see her get away from me. As far as possible... \nThen, she limped towards where I had pointed... \n and i couldn't see her anymore")
              go_home1 = input ("\nAs soon as she had disappeared from my line of sight...\nI had to go to a...\nany place where people are around! \n\nand at that moment...\n \n\"SHE IS NOT HERE!\" \nI heard her screaming far away. \"Should I run???\", I thought to myself... \nType \'RUN\' to get tf out of there!!! or \'STAY CALM\' to avoid giving her attention: ").lower()
              if go_home1 == "run":
                print("\n I began to run as fast as I could but then...\n\nShe jumped on my back. We began to struggle but her strength was something I never experienced. \nBefore I could even begin to process what was happen, I had been stabbed... bleeding out on the floor... my consciousness began to fade...")
                print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
              elif go_home1 == "stay calm":
                print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
            elif my_thoughts2 == "silent":
                print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
elif scared == "continue":
      saw = input ("\n \nI saw a woman walking in front of me. But she looked a little strange. \nI could see she looked crippled. She was limping and struggling to walk in front of me.\nContinue walking: Type \'CONTINUE\'to keep moving: ").lower()
      if saw == "continue":
        print("\nSince she was walking very slow, I soon caught up with her.")
        better = input ("\nI got closer and saw her better.. \nDescribe what I saw: Type \'DESCRIBE\'to explain what you see: ").lower()
        if better == "describe":
          print("\n\nShe was wearing dirty pink pajamas and looked as if all the joints in her body had been twisted. \nWorse, her hair was a mess and stickingout everywhere...")
          help1 = input ("\n\"HELP... "+name+"'\' she exclaimed. \nHow did she know my name? \n\nType \'STOP\' to stop and ask or \'CONTINUE\' to proceed: ").lower()
          if help1 == "stop":
            print("\n\nIt seemed so weird so I stopped walking...")
            she_calls = input ("\n\"HEEELP!!!\" she exclaimed again. Do I go to her or go the other way?\nType \'FIND OUT\' to approach her or \'TURN AROUND\' to go the other way: ").lower()
            if she_calls == "turn around":
              print("\n\nas I turned around, i felt her creep up behind me...\ncloser...\n\ncloser...\n\n\n and she put her hand on my shoulder... \nShe then screamed \"WHERE IS MY BABY?!?!?\"")
              my_thoughts = input("\nType \'answer\' to point to where the baby is or \'silent\' to give no response ").lower()
              if my_thoughts == "answer":
                print("\nI answered pointing as far as I could. \"Over there\", I said terrified")
                print("\nI wanted to see her get away from me. \nThen, she limped towards where I had pointed... \n and i couldn't see her anymore")
                go_home = input ("\nAs soon as she had disappeared from my line of sight...\nI had to go to a...\nany place where people are around! \n\nand at that moment...\n \n\"SHE IS NOT HERE!\" \nI heard her screaming far away. \"Should I run???\", I thought to myself... \nType \'RUN\' to get tf out of there!!! or \'STAY CALM\' to avoid giving her attention: ").lower()
                if go_home == "run":
                  print("\n I began to run as fast as I could but then...\n\nShe jumped on my back. We began to struggle but her strength was something I never experienced. \nBefore I could even begin to process what was happen, I had been stabbed... bleeding out on the floor... my consciousness began to fade... ")
                  print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
                elif go_home == "stay calm":
                  print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                  print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
              elif my_thoughts == "silent":
                print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
            elif she_calls == "find out":
              print("She screamed \"WHERE IS MY BABY?!?!?\"")
              print("\nI reached out to ask this crazy woman how she knew my name... \nI put my hands on her shoulder and before i could react, I felt a blade, as cold as ice, plunged into my chest...\n\nI had been stabbed... bleeding out on the floor... my consciousness began to fade...")
              print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
          elif help1 == "continue":
            print("\"I felt like i shouldn't get any closer to her nor did i have the guts to pass her by\" I thought to myself")
            print("You know, when people say that if you are really in shock, you can't evem scream...\n That was right...\n I froze there, no beong able to move at all.")
            print("she put her hand on my shoulder... \nShe then screamed \"WHERE IS MY BABY?!?!?\"")
            my_thoughts22 = input("\nType \'answer\' to point to where the baby is or \'silent\' to give no response ").lower()
            if my_thoughts22 == "answer":
              print("I answered pointing as far as I could. \"Over there\" I said terrified")
              print("I wanted to see her get away from me. \nThen, she limped towards where I had pointed... \n and i couldn't see her anymore")
              go_home = input ("\nAs soon as she had disappeared from my line of sight...\nI had to go to a...\nany place where people are around! \n\nand at that moment...\n \n\"SHE IS NOT HERE!\" \nI heard her screaming far away. \"Should I run???\", I thought to myself... \nType \'RUN\' to get tf out of there!!! or \'STAY CALM\' to avoid giving her attention: ").lower()
              if go_home == "run":
                print("\n I began to run as fast as I could but then...\n\nShe jumped on my back. We began to struggle but her strength was something I never experienced. \nBefore I could even begin to process what was happen, I had been stabbed... bleeding out on the floor... my consciousness began to fade...")
                print("""
 ▄▄▄▄    ▄▄▄      ▓█████▄    ▓█████  ███▄    █ ▓█████▄  ██▓ ███▄    █   ▄████ 
▓█████▄ ▒████▄    ▒██▀ ██▌   ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▓██▒ ██ ▀█   █  ██▒ ▀█▒
▒██▒ ▄██▒██  ▀█▄  ░██   █▌   ▒███   ▓██  ▀█ ██▒░██   █▌▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
▒██░█▀  ░██▄▄▄▄██ ░▓█▄   ▌   ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌░██░▓██▒  ▐▌██▒░▓█  ██▓
░▓█  ▀█▓ ▓█   ▓██▒░▒████▓    ░▒████▒▒██░   ▓██░░▒████▓ ░██░▒██░   ▓██░░▒▓███▀▒
░▒▓███▀▒ ▒▒   ▓▒█░ ▒▒▓  ▒    ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
▒░▒   ░   ▒   ▒▒ ░ ░ ▒  ▒     ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒  ▒ ░░ ░░   ░ ▒░  ░   ░ 
 ░    ░   ░   ▒    ░ ░  ░       ░      ░   ░ ░  ░ ░  ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
 ░            ░  ░   ░          ░  ░         ░    ░     ░           ░       ░ 
      ░            ░                            ░                             """)
              elif go_home == "stay calm":
                print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
            elif my_thoughts22 == "silent":
                print("\nI saw her running towards me and before I could react, she jumped at me... \n the next day... \n \n I don't remember anything from then on. I heard that my neighbor found me passed out on the ground and took me home.")
                print("""\
▄▄▄█████▓ ██░ ██ ▓█████    ▓█████  ███▄    █ ▓█████▄ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓█   ▀  ██ ▀█   █ ▒██▀ ██▌
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒███   ▓██  ▀█ ██▒░██   █▌
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒████▒▒██░   ▓██░░▒████▓ 
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ 
    ░     ▒ ░▒░ ░ ░ ░  ░    ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ 
  ░       ░  ░░ ░   ░         ░      ░   ░ ░  ░ ░  ░ 
          ░  ░  ░   ░  ░      ░  ░         ░    ░    
                                              ░      """)
