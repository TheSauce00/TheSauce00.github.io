### ONLINE BULLETIN SCREEN ###

transform loading_dot1a:
    yoffset 0
    pause 0.25
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform loading_dot2a:
    yoffset 0
    pause 0.5
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform loading_dot3a:
    yoffset 0
    pause 0.75
    linear 0.1 yoffset -100
    linear 0.2 yoffset 0
transform news_fade:
    on idle:
        alpha 1.0
        linear 0.15 alpha 0.75
    on hover:
        alpha 0.75
        linear 0.15 alpha 1.0
transform loading_start_:
    on show:
        alpha 1.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0
transform loading_trans_:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

screen show_bulletin:
    zorder 100
    modal True
    default load_screen_bullet = True
    add "#000000" alpha 0.9
    if selected_bullet2['img2'] == '' or len(selected_bullet2["text"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_bulletin")]

    else:
        frame:
            xalign 0.5
            yalign 0.5
            background None

            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 40
                text selected_bullet2['title'] size 50 color "#FFFFFF" bold True text_align 0.5 outlines [ (absolute(8), "#000", absolute(2), absolute(2)) ]

                imagebutton:
                    xalign 0.5
                    idle fetch_image(selected_bullet2['img2'])
                    action NullAction()

                viewport at loading_trans_:
                    xysize (2000, 750)
                    mousewheel True
                    vbox:
                        for i in selected_bullet2["text"]:
                            text i['text'] color "#FFFFFF" xsize 1500 text_align 0.5 outlines [ (absolute(8), "#000", absolute(2), absolute(2)) ]

        imagebutton:
            idle Text("{color=#808080}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            xalign 0.5
            yalign 1.0
            yoffset -50
            action [SetVariable("bullet_screen",False),Hide("show_bulletin")]

default selected_nl = None
default nl_screen = False
default nl_delay = False
screen show_newsletter:
    zorder 100
    modal True
    default load_screen_bullet = True
    add "#000000" alpha 0.9
    #text str(len(loaded_img_cache))
    if selected_bullet2["title"] == '' or len(selected_bullet2["imgs"]) == 0 or len(selected_bullet2["texts"]) == 0 or len(selected_bullet2["bulls"]) == 0 or len(selected_bullet2["dsc"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),SetVariable("selected_nl",None),Hide("show_newsletter")]

    else:
        if selected_bullet['id'] not in loaded_img_cache:
            timer 0.01 action Show("newsletter_image_load")

        if selected_nl != None:
            frame:
                xalign 0.0
                yalign 0.5
                background None

                add Transform(Solid("#000000", xysize=(2000, 850),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                viewport at loading_trans_:
                    xysize (2000, 750)
                    mousewheel True
                    xalign 0.0
                    yalign 0.5
                    xoffset 1225
                    yoffset -20
                    vbox:
                        xalign 0.0
                        yalign 0.5
                        #spacing 40
                        text selected_bullet2['title'] color "#FFFFFF" size 40 text_align 0.5 bold True

                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        for i in selected_bullet2["texts"]:
                            text i['nl_text'] color "#FFFFFF" size 25 text_align 0.5 bold False xsize 700

                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True
                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        for i in selected_bullet2["bulls"]:
                            vbox:
                                spacing 25
                                text i['title'] color "#FFFFFF" size 30 bold True xsize 600
                                for ii in i["texts"]:
                                    text ii['nl_text'] color "#FFFFFF" size 20 bold False xsize 600
                                text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        text "" color "#FFFFFF" size 20 text_align 0.5 bold True

                        for i in selected_bullet2["dsc"]:
                            text i['dsc_text'] color "#FFE300" size 15 bold True xsize 600

                vbox:
                    xalign 0.0
                    yalign 0.5
                    spacing 40
                    #text selected_bullet['title'] color "#FFFFFF" xsize 1500 text_align 0.5 bold True
                    for i in selected_bullet2["imgs"]:
                        if i == selected_nl:
                            #text i['text_top'] color "#FFFFFF" xsize 1500 text_align 0.5
                            imagebutton:
                                xalign 0.0
                                yalign 0.5
                                idle Transform(fetch_image(i['nl_img']),zoom=0.5)#NewsImage
                                action NullAction()
                            #text i['text_bottom'] color "#FFFFFF" xsize 1500 text_align 0.5

                    hbox:
                        xalign 0.0
                        yalign 0.5
                        xoffset 10
                        yoffset -65
                        spacing 10
                        if selected_bullet2["imgs"].index(selected_nl) == 0:
                            textbutton _("<") action [SetVariable("selected_nl",selected_bullet2["imgs"][-1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 55
                        else:
                            textbutton _("<") action [SetVariable("selected_nl",selected_bullet2["imgs"][selected_bullet2["imgs"].index(selected_nl)-1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 55


                        for i in selected_bullet2["imgs"]:
                            if selected_nl == i:
                                textbutton _(".") action [NullAction(),SetVariable("nl_delay",True)] text_size 200 text_idle_color "#FFFFFF" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75
                            else:
                                textbutton _(".") action [SetVariable("selected_nl",i),SetVariable("nl_delay",True)] text_size 200 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75

                        if selected_bullet2["imgs"].index(selected_nl) == len(selected_bullet2["imgs"])-1:
                            textbutton _(">") action [SetVariable("selected_nl",selected_bullet2["imgs"][0]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 55
                        else:
                            textbutton _(">") action [SetVariable("selected_nl",selected_bullet2["imgs"][selected_bullet2["imgs"].index(selected_nl)+1]),SetVariable("nl_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 55

            imagebutton:
                idle Text("{color=#808080}CLOSE", size = 50, bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ])
                hover Text("{color=#FFFFFF}CLOSE", size = 50, bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ])
                xalign 0.5
                yalign 1.0
                yoffset -15
                action [SetVariable("bullet_screen",False),SetVariable("selected_nl",selected_bullet2["imgs"][0]),Hide("show_newsletter")]
screen newsletter_image_load:
    zorder 999
    modal True
    default loading_images = False
    default load_go = False
    add "#000000" alpha 0.9
    add Text("LOADING IMAGES", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
    hbox:
        xalign 0.5 yalign 0.5
        spacing 50
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a


    if loading_images == False:
        timer 0.5 action SetScreenVariable("load_go",True)

    if load_go == True:
        for a in selected_bullet2['imgs']:
            $ batch_fetch_images(a['nl_img'])

    timer 1.0 action [SetVariable("selected_nl",selected_bullet2["imgs"][0]),Hide("newsletter_image_load")]

transform check_list_fade:
    alpha 0.5
default load_progress_ready = False
default check_show = False
screen show_progress:
    zorder 100
    modal True
    default load_screen_bullet = True
    default selected_check = 0
    add "#000000" alpha 0.9

    if len(selected_bullet2["progress"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_progress")]

    else:
        if selected_bullet['id'] not in loaded_img_cache:
            timer 0.01 action [SetVariable("load_progress_ready",False),SetVariable("check_show",False),Show("progress_image_load")]

        if load_progress_ready == True:
            if check_show == True:
                if len(selected_bullet2['progress']) > 0:
                    $ comp_per = []
                    for a in selected_bullet2['progress'][selected_check]['check']:
                        if a['status'] == "check":
                            $ comp_per.append(a)

                    $ per = int((float(len(comp_per)) / len(selected_bullet2['progress'][selected_check]['check'])) * 100)

                    hbox:
                        xoffset 15 yoffset 115
                        text "Version"  color "#FFFFFF" size 30 outlines [ (absolute(5), "#000", absolute(1.75), absolute(1.75)) ] bold False
                        text selected_bullet2['progress'][selected_check]['ver'] color "#FFFFFF" size 30 outlines [ (absolute(5), "#000", absolute(1.75), absolute(1.75)) ] bold False
                        text "-" color "#FFFFFF" size 30 outlines [ (absolute(5), "#000", absolute(1.75), absolute(1.75)) ] bold False
                        text selected_bullet2['progress'][selected_check]['proj'] color "#FFFFFF" size 30 outlines [ (absolute(5), "#000", absolute(1.75), absolute(1.75)) ] bold False
                        text " - LIVE PROGRESS - [per]%" color "#FFFFFF" size 30 outlines [ (absolute(5), "#000", absolute(1.75), absolute(1.75)) ] bold False

                    vbox:
                        xalign 1.0
                        frame:
                            background None
                            xsize 750
                            ysize 50
                            text "Still needs to be worked on -" color "#FFFFFF" size 25 text_align 0.5 xalign 1.0 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] xoffset -50
                            add Transform(fetch_image(persistent.current_news['box']),zoom=0.20) xalign 1.0
                        frame:
                            background None
                            xsize 750
                            ysize 50
                            text "A work in progress -" color "#FFFFFF" size 25 text_align 0.5 xalign 1.0 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] xoffset -50
                            add Transform(fetch_image(persistent.current_news['box']),zoom=0.20) xalign 1.0
                            add Transform(fetch_image(persistent.current_news['wip']),zoom=0.20) xalign 1.0
                        frame:
                            background None
                            xsize 750
                            ysize 50
                            text "Done! -" color "#FFFFFF" size 25 text_align 0.5 xalign 1.0 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] xoffset -50
                            add Transform(fetch_image(persistent.current_news['box']),zoom=0.20) xalign 1.0
                            add Transform(fetch_image(persistent.current_news['check']),zoom=0.20) xalign 1.0

                    frame:
                        xalign 0.5
                        yalign 0.5
                        background None
                        add Transform(Solid("#FFFFFF", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        viewport at loading_trans_:
                            xysize (1700, 750)#xysize (1890, 750)
                            mousewheel True
                            xalign 0.5
                            yalign 0.5
                            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        viewport at loading_trans_:
                            xysize (1700, 750)#xysize (1890, 750)
                            mousewheel True
                            xalign 0.5
                            yalign 0.5
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 40
                                for i in selected_bullet2['progress'][selected_check]['check']:
                                    hbox:
                                        spacing 2
                                        frame:
                                            background None
                                            xsize 100
                                            ysize 90
                                            add Transform(fetch_image(persistent.current_news['box']),zoom=0.35)
                                            if i['status'] == "":
                                                pass
                                            elif i['status'] == "wip":
                                                add Transform(fetch_image(persistent.current_news['wip']),zoom=0.35)
                                            elif i['status'] == "check":
                                                add Transform(fetch_image(persistent.current_news['check']),zoom=0.35)

                                        if i['status'] == "":
                                            text i['check'] color "#FFFFFF" text_align 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
                                        elif i['status'] == "wip":
                                            text i['check'] color "#FFFFFF" text_align 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
                                        elif i['status'] == "check":
                                            text i['check'] color "#FFFFFF" text_align 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] strikethrough True at check_list_fade

                            #vbox:
                                #for i in selected_bullet["text"]:
                                    #text i['text'] color "#FFFFFF" xsize 1500 text_align 0.5

                        if len(selected_bullet2['progress']) > 1:

                            imagebutton:
                                idle Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=1.0)#NewsImage
                                hover Transform(fetch_image(persistent.current_news['arrow_hover']),xzoom=1.0)#NewsImage
                                xalign 0.0 yalign 0.5
                                if selected_check == 0:
                                    action [SetVariable("check_show",False),SetScreenVariable("selected_check",len(selected_bullet2['progress'])-1),Show("progress_image_load")]
                                else:
                                    action [SetVariable("check_show",False),SetScreenVariable("selected_check",selected_check-1),Show("progress_image_load")]

                            imagebutton:
                                idle Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=-1.0)#NewsImage
                                hover Transform(fetch_image(persistent.current_news['arrow_hover']),xzoom=-1.0)#NewsImage
                                xalign 1.0 yalign 0.5
                                if selected_check == len(selected_bullet2['progress'])-1:
                                    action [SetVariable("check_show",False),SetScreenVariable("selected_check",0),Show("progress_image_load")]
                                else:
                                    action [SetVariable("check_show",False),SetScreenVariable("selected_check",selected_check+1),Show("progress_image_load")]
                        else:
                            imagebutton at check_list_fade:
                                idle Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=1.0)#NewsImage
                                hover Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=1.0)#NewsImage
                                xalign 0.0 yalign 0.5
                                action NullAction()

                            imagebutton at check_list_fade:
                                idle Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=-1.0)#NewsImage
                                hover Transform(fetch_image(persistent.current_news['arrow_idle']),xzoom=-1.0)#NewsImage
                                xalign 1.0 yalign 0.5
                                action NullAction()
                else:
                    frame:
                        xalign 0.5
                        yalign 0.5
                        background None
                        add Transform(Solid("#FFFFFF", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        text " - NO PLANNED UPDATES AT THE MOMENT - " xoffset 275 yoffset 25 color "#FFFFFF" size 60 text_align 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]

                imagebutton:
                    idle Text("{color=#808080}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
                    hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
                    xalign 0.5
                    yalign 1.0
                    yoffset -50
                    action [SetVariable("bullet_screen",False),Hide("show_progress")]
screen progress_image_load:
    zorder 999
    modal True
    default loading_images = False
    default load_go = False
    add "#000000" alpha 0.9
    add Text("LOADING PROGRESS", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
    hbox:
        xalign 0.5 yalign 0.5
        spacing 50
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
        add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a

    if load_progress_ready != True:
        if loading_images == False:
            timer 0.5 action SetScreenVariable("load_go",True)

        if load_go == True:
            $ batch_fetch_images(persistent.current_news['box'])
            $ batch_fetch_images(persistent.current_news['wip'])
            $ batch_fetch_images(persistent.current_news['check'])
            $ batch_fetch_images(persistent.current_news['arrow_idle'])
            $ batch_fetch_images(persistent.current_news['arrow_hover'])

        timer 1.0 action [SetVariable("load_progress_ready",True),SetVariable("check_show",True),Hide("progress_image_load")]
    else:
        timer 0.5 action [SetVariable("load_progress_ready",True),SetVariable("check_show",True),Hide("progress_image_load")]

screen show_patrons:
    zorder 100
    modal True
    add "#000000" alpha 0.9

    $ active_patrons = []
    for a in selected_bullet2["tiers"]:
        #if a['active'] == "True" and a['id'] in persistent.branch_check:
        $ active_patrons.append(a)

    if len(selected_bullet2["tiers"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_patrons")]
    else:
        frame:
            xalign 0.5
            yalign 0.5
            background None
            add Transform(Solid("#FFFFFF", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 10
                for i in selected_bullet2["tiers"]:
                    frame:
                        background None
                        xysize (400, 750)
                        xalign 0.5
                        yalign 0.5
                        viewport at loading_trans_:
                            xysize (400, 750)
                            xalign 0.5
                            yalign 0.5
                            add Transform(Solid(i['color'], xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
                        viewport at loading_trans_:
                            xysize (400, 750)
                            mousewheel True
                            xalign 0.5
                            yalign 0.5
                            vbox:
                                frame:
                                    background None
                                    xysize (400, 50)
                                    text i['tier'] color i['text_color'] size 25 text_align 0.5 xalign 0.5 bold True
                                    text "_________________________________" color i['text_color'] size 30 text_align 0.5 xalign 0.5 kerning -5 yoffset 0
                                if len(i["patrons"]) > 0:
                                    for p in i["patrons"]:
                                        text p color i['text_color'] size 20 text_align 0.5 xalign 0.5
                                else:
                                    text "Error Retrieving Patrons List" color i['text_color'] size 20 text_align 0.5 xalign 0.5 yalign 0.5 yoffset 300

        imagebutton:
            idle Text("{color=#808080}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            xalign 0.5
            yalign 1.0
            yoffset -50
            action [SetVariable("bullet_screen",False),Hide("show_patrons")]

screen show_purchases:
    zorder 100
    modal True
    add "#000000" alpha 0.9

    #$ active_patrons = []
    #for a in selected_bullet2["tiers"]:
        ##if a['active'] == "True" and a['id'] in persistent.branch_check:
        #$ active_patrons.append(a)

    if len(selected_bullet2["listing"]) == 0:
        add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
        if load_screen_bullet == True:
            add Text("LOADING BULLETIN", size=25, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) xalign 0.5 yalign 0.5 yoffset 150
            hbox:
                xalign 0.5 yalign 0.5
                spacing 50
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot1a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot2a
                add Text(".", size=300, color="#FFFFFF", bold=True, outlines = [ (absolute(8), "#000", absolute(2.5), absolute(2.5)) ]) at loading_dot3a
            timer 2.0 action SetScreenVariable("load_screen_bullet",False)
        else:
            text "- Error -" size 100 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            text "Bulletin Not Available" size 50 color "#808080" text_align 0.5 xalign 0.5 yalign 0.5 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset 150 #xoffset 5
            timer 1.0 action [SetVariable("bullet_screen",False),Hide("show_purchases")]
    else:
        frame:
            xalign 0.5
            yalign 0.5
            background None
            add Transform(Solid("#FFFFFF", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            text "Available for Purchase on itch.io!" size 50 color "#FFFFFF" yoffset 50 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
            viewport at loading_trans_:
                xysize (1700, 750)#xysize (1890, 750)
                mousewheel True
                xalign 0.5
                yalign 0.5
                add Transform(Solid("#000000", xysize=(2000, 750),xalign=0.5),alpha=0.95) xalign 0.5 yalign 0.5
            viewport at loading_trans_:
                xysize (1700, 750)#xysize (1890, 750)
                mousewheel True
                xalign 0.5
                yalign 0.5
                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 5
                    for i in selected_bullet2['listing']:
                        frame:
                            background None
                            xsize 1700
                            ysize 150
                            hbox:
                                add Transform(fetch_image(i['icon']),zoom=0.5)
                                vbox:
                                    text i['title'] color "#FFFFFF" size 45 outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] yoffset -5
                                    text i['type'] size 25 color "#8C8C8C" yoffset 25
                                if i['button'] == '':
                                    pass
                                elif i['button'] == 'COMING SOON':
                                    text " - " yoffset 10
                                    textbutton i['button']:
                                        text_idle_color "#FFFFFF"
                                        text_hover_color i["color"]
                                        text_size 45
                                        text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
                                        yoffset -5
                                        action NullAction()
                                elif i['button'] == 'UNAVAILABLE':
                                    text " - " yoffset 10
                                    textbutton i['button']:
                                        text_idle_color "#727272"
                                        text_hover_color "#727272"
                                        text_size 45
                                        text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
                                        yoffset -5
                                        action NullAction()
                                else:
                                    text " - " yoffset 10
                                    textbutton i['button']:
                                        text_idle_color "#FFFFFF"
                                        text_hover_color i["color"]
                                        text_size 45
                                        text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ]
                                        yoffset -5
                                        if i["link"] == "":
                                            action NullAction()
                                        else:
                                            action OpenURL(i["link"])


        imagebutton:
            idle Text("{color=#808080}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            hover Text("{color=#FFFFFF}CLOSE", size = 75, bold=True, outlines = [ (absolute(8), "#000", absolute(2), absolute(2)) ])
            xalign 0.5
            yalign 1.0
            yoffset -50
            action [SetVariable("bullet_screen",False),Hide("show_purchases")]

default selected_bullet = None
default selected_bullet2 = None
default bullet_screen = False
default bullet_delay = False
screen bulletin_board:
    timer 0.01 action Function(update_news)

    $ active_bulletins = []
    if persistent.news != None:
        for a in persistent.current_news['main_bulletin']:
            if a['active'] == "True" and a['id'] in persistent.branch_check:
                $ active_bulletins.append(a)

    viewport at loading_trans_:
        xysize (750, 175)
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15
        add "#000000c0" alpha 0.75
        add "#FFFFFF" alpha 0.5
    viewport at loading_trans_:
        xysize (750, 175)
        mousewheel True
        xalign 1.0
        yalign 0.0
        xoffset -50
        yoffset 15

        vbox:
            frame:
                background None
                ysize 5
                text ""
            if persistent.current_news == None:
                text "OFFLINE" size 75 color "#808080" outlines [ (absolute(7), "#000", absolute(4), absolute(4)) ] bold False xoffset 200 yoffset 40
            else:
                if persistent.current_news['maintenance'] == 'True':
                    text "* Maintenance Being Done *" size 50 color "#808080" outlines [ (absolute(7), "#000", absolute(4), absolute(4)) ] bold False xoffset 10 yoffset 55
                else:
                    if len(active_bulletins) == 0:
                        text "* Maintenance Being Done *" size 50 color "#808080" outlines [ (absolute(7), "#000", absolute(4), absolute(4)) ] bold False xoffset 10 yoffset 55
                    else:
                        timer 0.01 action SetVariable("selected_bullet",active_bulletins[0])
                        if selected_bullet != None:
                            imagebutton:
                                idle fetch_image(selected_bullet['img'])
                                yoffset -5
                                if selected_bullet['bull_type'] == "screen_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_bulletin")]
                                elif selected_bullet['bull_type'] == "web_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),OpenURL(selected_bullet["link"])]
                                elif selected_bullet['bull_type'] == "newsletter_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_newsletter")]
                                elif selected_bullet['bull_type'] == "check_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_progress")]
                                elif selected_bullet['bull_type'] == "patron_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_patrons")]
                                elif selected_bullet['bull_type'] == "purchase_link":
                                    action [Function(set_bulletin),SetVariable("bullet_screen",True),Show("show_purchases")]
                                else:
                                    action NullAction()

    if bullet_delay != False:
        timer 0.25 action SetVariable("bullet_delay",False)

    if persistent.current_news == None:
        hbox:
            xalign 0.5
            xoffset 550
            yoffset 150
            spacing 25
            textbutton _("<") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25

            textbutton _(".") action NullAction() text_size 100 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75

            textbutton _(">") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25
    else:
        if persistent.current_news['maintenance'] == 'True' or len(active_bulletins) == 0:
            hbox:
                xalign 0.5
                xoffset 550
                yoffset 150
                spacing 25
                textbutton _("<") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25

                textbutton _(".") action NullAction() text_size 100 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75

                textbutton _(">") action NullAction() text_size 50 text_idle_color "#757575" text_hover_color "#757575" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25
        else:
            if selected_bullet != None:
                if bullet_screen == False:
                    if active_bulletins.index(selected_bullet) == len(active_bulletins)-1:
                        if bullet_delay == False:
                            timer 5.0 repeat True action SetVariable("selected_bullet",active_bulletins[0])
                    else:
                        if bullet_delay == False:
                            timer 5.0 repeat True action SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)+1])

                hbox:
                    xalign 0.5
                    xoffset 550
                    yoffset 150
                    spacing 25
                    if active_bulletins.index(selected_bullet) == 0:
                        textbutton _("<") action [SetVariable("selected_bullet",active_bulletins[-1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25
                    else:
                        textbutton _("<") action [SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)-1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25


                    for i in active_bulletins:
                        if selected_bullet == i:
                            textbutton _(".") action [NullAction(),SetVariable("bullet_delay",True)] text_size 100 text_idle_color "#FFFFFF" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75
                        else:
                            textbutton _(".") action [SetVariable("selected_bullet",i),SetVariable("bullet_delay",True)] text_size 100 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75

                    if active_bulletins.index(selected_bullet) == len(active_bulletins)-1:
                        textbutton _(">") action [SetVariable("selected_bullet",active_bulletins[0]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25
                    else:
                        textbutton _(">") action [SetVariable("selected_bullet",active_bulletins[active_bulletins.index(selected_bullet)+1]),SetVariable("bullet_delay",True)] text_size 50 text_idle_color "#757575" text_hover_color "#FFFFFF" text_outlines [ (absolute(5), "#000", absolute(2), absolute(2)) ] ysize 75 yoffset 25









label quit:
    $ persistent.news = None
    $ persistent.current_news = None
    $ delete_file()
    $ cleanup_temp_files()
