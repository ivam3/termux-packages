var state = new GameState();
//read cookie if one exists
var current_room = state.getCurrentRoom();
// var current_room = KernelFiles;
var man_pages = {"cd": "The old man's voice echoes in your head as if from a great distance: \n"+
"(Choose Destination) Use \"cd\" to move about the world. \n" +
"Command Input: cd LOCATION \n" +
 "Rememberrrrrr...", 
"mv": "The old man's voice echoes in your head as if from a great distance: \n" + 
"(MoVe). \n Use \"mv\" to move an object to a new location. \n Command Input:" + 
"mv OBJECT NEWLOCATION \n" + 
"Rememberrrrrr...",
"ls": "The old man's voice echoes in your head as if from a great distance: \n" + 
"(Look at your Surroundings). \n Use \"ls\" to look at what’s in a certain location. " +
"Either your current location or (rarely) you may have look into a location to see "+
"what's in it. \n" + 
" Command Input: \n" + 
"ls          (for current location) \n" + 
"-OR- \n" + 
"ls LOCATION     (for locations you that you cannot \"cd\" into)\n" + 
"Rememberrrrrr...", 
"less": "The old man's voice echoes in your head as if from a great distance: \n"+
"(Look at, Examine, or Speak to Something). \nUse \"less\" to look at what’s in a "+
"certain location. Either your current location or (rarely) you may have look into a "+
"location to see what is in it. \n" + 
"Command Input: less ITEM\n" +
"Rememberrrrrr...", 
"man": "I'm the old man dangit! You can't try to get more information about me. Here are all the commands you can man: cd, ls, rm, mv, exit, help, man, touch, grep, pwd.", 
"help": "Type \"man COMMAND\" if you forget how to use a command.", 
"exit": "The old man's voice echoes in your head as if from a great distance:\n" + 
"(exit) \n" + 
"Use \"exit\" to exit the game permanently. \n" + 
"Command Input: \n" + 
"exit \n" + 
"Rememberrrrrr...", 
"cp": "The old man's voice echoes in your head as if from a great distance:\n" +
"(CoPy)\n" + 
"Use \"cp\" to duplicate an item. \n" + 
"Command Input:\n" + 
"cp ITEM NEWNAME \n" +
"Rememberrrrrr...", 
"pwd": "The old man's voice echoes in your head as if from a great distance: \n" + 
"(Print Where i Do stuff) \n" +
"To remind yourself where you currently are.\n" + 
"Command Input: \n" + 
"pwd \n" + 
"Rememberrrrrr...",
"grep": "The old man's voice echoes in your head as if from a great distance:\n" +
"(grep) \n" + 
"Use \"grep\" to command your minion to help search through text for you.\n" + 
"Command Input: \n" + 
"grep WORDTOSEARCH PLACETOSEARCH \n" +
"Rememberrrrrr...",
"touch": "The old man's voice echoes in your head as if from a great distance:\n"+
"(Touch) gives you the artisan's touch to create new objects.\n" +
"Use \"touch\" to create new objects in the world.\n" +
"Command Input:\n" + 
"touch OBJECT \n" + 
"Rememberrrrrr...", 
"tellme": "The old man's voice echoes in your head as if from a great distance:\n"+
"(tellme combo) tells you the combination for the AthenaCluster rooms at MIT.\n"+
"Command Input:\n"+
"tellme combo\n"+
"Rememberrrrrr..."}

$(document).ready(function() {
    $('#term').terminal(function(input, term) {
        var split = input.split(" ");
        var command = split[0].toString();
        var args = split.splice(1,split.length);
        var exec = true;
        if( current_room.commands.indexOf(command) > -1 ){ //Could use current_room.hasOwnProperty(command)
            var prev_room_to_test = current_room;
            if (args.length > 0 && args[0].indexOf("/") > 0){
                var rooms_in_order = args[0].split("/");
                var cur_room_to_test = current_room;
                for (var i = 0; i < rooms_in_order.length; i++){
                    prev_room_to_test = cur_room_to_test;
                    var room_to_cd = rooms_in_order[i];
                    if (i > 0 && rooms_in_order[i-1] === "~"){
                        cur_room_to_test = Home.can_cd(room_to_cd)
                    } else if (room_to_cd === "~"){
                        cur_room_to_test = Home;
                    } else {
                        cur_room_to_test = cur_room_to_test.can_cd(room_to_cd);
                    }
                    if ((command === "cd" || command === "ls") && cur_room_to_test === false){
                        term.echo("That is not reachable from here.");
                        exec = false;
                    }
                }
                args[0] = cur_room_to_test.room_name;
            }
            if (exec){
                var text_to_display = prev_room_to_test[command](args);
                if (text_to_display){
                    term.echo(text_to_display);
                }
                if (command in current_room.cmd_text){
                    term.echo(current_room.cmd_text[command]);
                }
            }
        }
        else{
            term.echo("Command '"+command+"' not found in room '"+current_room.room_name+"'");
        }
    }, { history: true,                     // Keep user's history of commands
        prompt: '>',                        // Text that prefixes terminal entries
        name: 'terminus_terminal',          // Name of terminal
                                            // Signiture to include at top of terminal
        greetings:"Welcome! If you are new to the game, here are some tips: \n\n" +
		"Look at your surroundings with the command \"ls\". \n" +
		"Move to a new location with the command \"cd LOCATION\" \n" +
		"You can backtrack with the command \"cd ..\". \n" +
		"Interact with things in the world with the command \"less ITEM\" \n\n" +
        "If you forget where you are, type \"pwd\" \n\n" + 
		"Go ahead, explore. We hope you enjoy what you find. Do ls as your first command.\n",
        exit: false,                        // Disable 'exit' command
        clear: true,                       // Disable 'clear' command
        });
    
    // Clear history on page reload
    $("#term").terminal().history().clear();
    //Give term focus (Fixes weird initial draw issue)
    $("#term").click();
    //Tab Completion FOR LAST ARGUMENT
    $(window).keyup(function(event){
        if(event.keyCode == 9){
            var command = $("#term").terminal().get_command().replace(/\s+$/,"");
            var split_command = command.split(" ");
            var first_arg = split_command[0]
            var last_arg = split_command.pop();
            //Start in a room, try to move through path, and if we get to the end
            // check whether a room/item could complete our trip
            
            //Get starting room
            var search_room;
            if(last_arg.substring(0,1) == "~"){
                search_room = jQuery.extend(true, {}, Home);
            }
            else{
                search_room = jQuery.extend(true, {}, current_room);
            }
            //Iterate through each room
            var path_rooms = last_arg.split("/");
            var new_room;
            var incomplete_room;
            var substring_matches = [];
            for (room_num=0;room_num<path_rooms.length;room_num++)
            {
                new_room = search_room.can_cd(path_rooms[room_num]);
                if(new_room){
                    search_room = new_room;
                }
                else{
                    //We've made it to the final room,
                    // so we should look for things to complete our journey
                    if(room_num == path_rooms.length-1){
                        //IF cd, ls, cp, mv, less
                        //Compare to this room's children
                        if(first_arg == "cd" ||
                            first_arg == "ls" ||
                            first_arg == "mv")
                        {
                            for(child_num = 0; child_num<search_room.children.length; child_num++){
                                if(search_room.children[child_num].room_name.match("^"+path_rooms[room_num])){
                                    substring_matches.push(search_room.children[child_num].room_name);
                                }
                            }
                        }
                        //IF cp, mv, less, grep, touch
                        //Compare to this room's items
                        if(first_arg == "cp" ||
                            first_arg == "mv" ||
                            first_arg == "less" ||
                            first_arg == "grep" ||
                            first_arg == "touch" ||
                            first_arg == "rm" ||
                            first_arg == "sudo")
                        {
                            for(item_num = 0; item_num<search_room.items.length; item_num++){
                                if(search_room.items[item_num].itemname.match("^"+path_rooms[room_num])){
                                    substring_matches.push(search_room.items[item_num].itemname);
                                }
                            }
                        }
                        
                        //If one match exists
                        if(substring_matches.length == 1){
                            path_rooms.pop();
                            path_rooms.push(substring_matches[0]);
                            split_command.push(path_rooms.join("/"))
                            $("#term").terminal().set_command(split_command.join(" "));
                        }
                        //If multiple matches exist
                        else if(substring_matches.length > 1){
                            //Search for longest common substring (taken from: http://stackoverflow.com/questions/1837555/ajax-autocomplete-or-autosuggest-with-tab-completion-autofill-similar-to-shell/1897480#1897480)
                            var lCSindex = 0
                            var i, ch, memo
                            do {
                                memo = null
                                for (i=0; i < substring_matches.length; i++) {
                                    ch = substring_matches[i].charAt(lCSindex)
                                    if (!ch) break
                                    if (!memo) memo = ch
                                    else if (ch != memo) break
                                }
                            } while (i == substring_matches.length && ++lCSindex)

                            var longestCommonSubstring = substring_matches[0].slice(0, lCSindex)
                            //If there is a common substring...
                            if(longestCommonSubstring != ""){
                                //If it already matches the last snippit, then show the options
                                if(path_rooms[room_num] == longestCommonSubstring){
                                    split_command.push(last_arg)                                                    //Join final argument to split_command
                                    $("#term").terminal().echo(">"+split_command.join(" ").replace(/\s+$/,""));     //Print what the user entered
                                    $("#term").terminal().echo(substring_matches.join(" "));                        //Print the matches
                                    $("#term").terminal().set_command(split_command.join(" ").replace(/\s+$/,""));  //Set the text to what the user entered
                                }
                                //Otherwise, fill in the longest common substring
                                else{
                                    path_rooms.pop();                           //Pop final snippit
                                    path_rooms.push(longestCommonSubstring);    //Push longest common substring
                                    split_command.push(path_rooms.join("/"))    //Join room paths
                                    $("#term").terminal().set_command(split_command.join(" ")); //Set the terminal text to this auto-completion
                                }
                            }
                            //Otherwise, there is no common substring.  Show all of the options.
                            else{
                                split_command.push(last_arg)                                                    //Join final argument to split_command
                                $("#term").terminal().echo(">"+split_command.join(" ").replace(/\s+$/,""));     //Print what the user entered
                                $("#term").terminal().echo(substring_matches.join(" "));                        //Print the matches
                                $("#term").terminal().set_command(split_command.join(" ").replace(/\s+$/,""));  //Set the text to what the user entered
                            }
                        }
                        //If no match exists
                        else{
                            //DO NOTHING (except remove TAB)
                            $("#term").terminal().set_command(command.replace(/\s+$/,""));
                        }
                    }
                    else{
                        //DO NOTHING (except remove TAB)
                        $("#term").terminal().set_command(command.replace(/\s+$/,""));
                    }
                }
            }
        }
    });
});