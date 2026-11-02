/*
 * Here are the parameters and values:
 * mvBoulder -- 1 means DankRoom and Tunnel are connected. Also means that the 
 			Boulder is in the SmallHole
 * pullLever -- Library and BackRoom are connected
 * AthenaComboEntered -- currently in Athena cluster
 * rmLargeBoulder -- RockyPath and Farm are connected. Also means that the LargeBoulder
 			has been removed
 * HouseMade -- Clearing and House are connected (user has made a House)
 * rmBrambles -- Clearing and OminousLookingPath are connected. Also means that 
 			ThornyBrambles have been removed
 * openSlide -- CaveOfDisgtruntledTrolls and Slide are connected. Also means that the
 			UglyTroll has been rm'ed or mv'ed
 * touchGear -- Gear was made in ArtisanShop, Artisan text changed
 * FiveGearsCopied -- five Gears copied in ArtisanShop, Artisan text changed
 * CornCopied -- corn copied in Farm
 * touchPlank -- Plank made in BrokenBridge
 * sudoComplete -- entered paradise (current location is paradise)
 */

function GameState(){
	//game starts at home unless loaded from cookie
	this.currentRoom = Home; 
	this.params = {};
};

//this function reads from a cookie if one exists
GameState.prototype.getCurrentRoom = function() {
	//by default the new room is just the current room
	var newRoomToSet=this.currentRoom;

	//if there is a cookie, the newRoomToSet is read from the cookie
	var cookieval=this.readCookie();
	if (cookieval){
		//parse the cookie. right now it is only the current room name
		var cookieargs = cookieval.split("=");
		var room_name_to_set = cookieargs.splice(0, 1);
		var cookie_params = cookieargs;
		for (var i = 0; i < cookie_params.length; i++){
			var param_pair = cookie_params[i].split(":");
			this.params[param_pair[0]] = param_pair[1];
			this.applyState(param_pair[0], true);
		}
		newRoomToSet=window[room_name_to_set];
	}

	//call setCurrentRoom to reset the expiration date on the cookie
	this.setCurrentRoom(newRoomToSet);
	return this.currentRoom;
};

GameState.prototype.setCurrentRoom = function(newRoom){
	this.currentRoom=newRoom;

	//when you call this function, set the cookie in the browser
	var date = new Date();
	//by default, cookies active for a week
	date.setTime(date.getTime()+(7*24*60*60*1000));
	document.cookie = "terminuscookie="+this.getState()+"; expires="+date.toGMTString()+"; path=/";
};

GameState.prototype.getState = function(){
	//for anything in the state, if it is not written in the cookie explicitly, it's value is 0
	var param_string = "";
	for (var key in this.params){
		if (this.params.hasOwnProperty(key)){
			param_string += key + ":" + this.params[key] + "=";
		}
	}
	return this.currentRoom.toString() + "=" + param_string;
};

GameState.prototype.update = function(name_prop, val){
	this.params[name_prop] = val;
};

GameState.prototype.readCookie = function(){
	var nameCookie = "terminuscookie";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameCookie) == 0) 
			return c.substring(nameCookie.length + 1,c.length);
	}
	return null;
};

GameState.prototype.applyState = function(param_name, replay){
	var re = (typeof replay === 'undefined') ? false : replay;
	state.update(param_name, "1");
	switch(param_name){
		case "mvBoulder": 
			link_rooms(DankRoom, Tunnel);
			SmallHole.addItem(Boulder);
			if (re) DankRoom.removeItem("Boulder");
			break;
		case "pullLever":
			link_rooms(Library, BackRoom);
    		break;
    	case "rmLargeBoulder":
    		link_rooms(RockyPath, Farm);
    		if (re) RockyPath.removeItem("LargeBoulder");
    		break;
    	case "touchGear":
    		Artisan.addCmdText("less", "Well that’s lovely, thank you, but you can’t expect me to make\
anything with just one gear! Can’t you copy it?\n\
...\n\
*sigh* I can see you are going to need a lot of training. Just say “cp [ITEM] [NEWITEM]”.\
[ITEM]’s the name of the item that you want copy, and [NEWITEM]’s the new name of the\
copy, got it? Then poof! You’ll have shiny new item. I need five more gears so you’d better\
get started! Just call them gear1, gear2, gear3, gear4, and gear5, please.");
    		ArtisanShop.addCommand("cp");
    		if (re) ArtisanShop.addItem(new Item("Gear", "This is a Gear","item_gear.gif"));
    		else ArtisanShop.getItemFromName("Gear").changePicName("item_gear.gif");
    		break;
    	case "FiveGearsCopied":
    		Artisan.addCmdText("less", "Ha, finished already? I guess you learn fast. Well, \
thanks for your assistance.");
    		if (re){
	    		ArtisanShop.addItem(new Item("gear1", "This is a Gear","item_gear.gif"));
	    		ArtisanShop.addItem(new Item("gear2", "This is a Gear","item_gear.gif"));
	    		ArtisanShop.addItem(new Item("gear3", "This is a Gear","item_gear.gif"));
	    		ArtisanShop.addItem(new Item("gear4", "This is a Gear","item_gear.gif"));
	    		ArtisanShop.addItem(new Item("gear5", "This is a Gear","item_gear.gif"));
    		}
    		break;
    	case "CornCopied":
    	    Farmer.addCmdText("less", "It’s a miracle! Thank you, friend. May the Admin bless you.");
    	    if (re) Farm.addItem(new Item("AnotherEarOfCorn", "This is AnotherEarOfCorn"));
    	    break;
    	case "HouseMade":
    		if (re) Clearing.addChild(new Room("House", "This is a House"));
    		Clearing.getChildFromName("House").addCmdText("cd", "You are entering the House that you made.");
  	 		Clearing.getChildFromName("House").addCmdText("ls", "You made this house for the man. How thoughtful of you!");
  		  	Clearing.removeCmdText("cd");
    		Clearing.changeIntroText("There's a small grassy clearing here, with a man sitting on a \
stone, weeping. Behind him is a pile of rubble and a small white house.");
    		CryingMan.addCmdText("less", "Thank you for making me the House!  Why am I still crying?  These are tears of joy.  Can't a man openly express his emotions?");
    		break;
    	case "touchPlank":
    		Clearing.addCommand("cd");
    		Clearing.removeCmdText("cd");
    		BrokenBridge.removeCmdText("cd");
    		BrokenBridge.changeIntroText("A creaky rope bridges stretches across a chasm.");
    		if (re) BrokenBridge.addItem(new Item("Plank","This is a Plank.","item_plank.gif"));
    		else BrokenBridge.getItemFromName("Plank").changePicName("item_plank.gif");
    		break;
    	case "rmBrambles":
    		link_rooms(OminousLookingPath, CaveOfDisgruntledTrolls) ;
    		if (re) OminousLookingPath.removeItem("ThornyBrambles");
    		break;
    	case "sudoComplete":
    		KernelFiles.removeCommand("IHTFP");
    		KernelFiles.removeCmdText("IHTFP");
    		link_rooms(KernelFiles, Paradise);
    		enterRoom(Paradise);
    		break;
    	case "openSlide":
    		Slide.addCommand("cd");
    		Slide.addCmdText("cd", "It's just a Slide. Keep going. You're almost at the KernelFiles.");
    		if (re) CaveOfDisgruntledTrolls.removeItem("UglyTroll");
    		break;
    	case "AthenaComboEntered":
    		AthenaCluster.addCommand("ls");
    		AthenaCluster.removeCmdText("ls");
		    AthenaCluster.addCommand("cd");
		    // AthenaCluster.addCmdText("cd", "You have correctly entered the cluster combo. You may enter.");
		    enterRoom(AthenaCluster);
		    MIT.removeCommand("terminus");
		    MIT.removeCmdText("terminus");
		    break;
		case "addMagicLocker": 
			link_rooms(Home, MagicLocker);
			break;
		default: 
			break;
	};
};