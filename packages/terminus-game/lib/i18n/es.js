'use strict';

const PAIRS = new Map(require('./es-pairs.json'));

const MESSAGES = new Map([
  ['That is not reachable from here.', 'No se puede llegar desde aquí.'],
  ["You can't move to multiple locations.", 'No puedes moverte a varias ubicaciones a la vez.'],
  ['You have come Home!', '¡Has vuelto a Home!'],
  ['You are at the first room.', 'Estás en la primera sala.'],
  ['That is not a valid object to look at.', 'Ese no es un objeto válido para mirar.'],
  ['Pick a different item to less.', 'Elige otro objeto para mirar.'],
  ['Must ask the man about something to receive a response.', 'Debes preguntarle algo al hombre para recibir una respuesta.'],
  ['there is no man page for that command', 'no hay página de manual para ese comando'],
  ["Type 'man' to ask the man for help", "Escribe 'man' para pedir ayuda al hombre"],
  ['You need to move thing A to place B. Use mov [thingA] [placeB].', 'Necesitas mover la cosa A al lugar B. Usa mv [cosaA] [lugarB].'],
  ['Must be a valid item and location to move it.', 'Debe ser un objeto y una ubicación válidos para moverlo.'],
  ['You must remove a particular item', 'Debes eliminar un objeto concreto'],
  ['That item cannot be removed', 'Ese objeto no se puede eliminar.'],
  ["That's not a valid object to remove.", 'Ese no es un objeto válido para eliminar.'],
  ['Not a valid item to search in.', 'No es un objeto válido en el que buscar.'],
  ["You haven't learned this spell yet.", 'Aún no has aprendido este hechizo.'],
  ['You must touch something in particular.', 'Debes tocar algo en concreto.'],
  ["You haven't touched anything. Check your syntax.", 'No has tocado nada. Revisa tu sintaxis.'],
  ['Incorrect syntax. Ask the OldMan for help.', 'Sintaxis incorrecta. Pide ayuda al OldMan.'],
  ['No item of that name to copy.', 'No hay ningún objeto con ese nombre para copiar.'],
  ["The combination is 'terminus' (without the quotes).", "La combinación es 'terminus' (sin las comillas)."],
  ['You have not learned this spell yet', 'Todavía no has aprendido este hechizo.'],
  ['Wrong syntax. Read the instructions again.', 'Sintaxis incorrecta. Lee las instrucciones de nuevo.'],
  ['You cannot cast this spell here.', 'No puedes lanzar este hechizo aquí.'],
  ['Wrong password.', 'Contraseña incorrecta.'],
  ['This is not a valid spell.', 'Este no es un hechizo válido.'],
  ['No valid locker of that name.', 'No hay un casillero válido con ese nombre.'],
  ['This is a simple room', 'Esta es una sala sencilla.'],
  ['This is a generic item', 'Es un objeto genérico.'],
  ['This is a House', 'Esta es una House.'],
  ['You are entering the House that you made.', 'Estás entrando en la House que construiste.'],
  ['You made this house for the man. How thoughtful of you!', 'Construiste esta casa para el hombre. ¡Qué detalle por tu parte!'],
  ['You have correctly entered the password. You are now in Paradise. Take a look around, and congratulations.', 'Has introducido la contraseña correctamente. Ya estás en Paradise. Echa un vistazo y enhorabuena.'],
  ['You have correctly entered the cluster combo. Entering the AthenaCluster.', 'Has introducido correctamente la combinación del clúster. Entrando en AthenaCluster.'],
  [' Locations:', ' Lugares:'],
  [' Items:', ' Objetos:']
]);

const PATTERNS = [
  [/^You are in (.+)\.$/gm, 'Estás en $1.'],
  [/^This is a (.+?)\.?$/gm, 'Esto es $1.'],
  [/^ Locations:/gm, ' Lugares:'],
  [/^ Items:/gm, ' Objetos:'],
  [/^You have moved to (.+?)\. ([\s\S]*)$/, (match, room, intro) =>
    'Te has movido a ' + room + '. ' + translate(intro)],
  [/^Moved (.+?) to (.+)\.$/gm, 'Moviste $1 a $2.'],
  [/^Just copied (.+?) into (.+)\.$/gm, 'Acabas de copiar $1 en $2.'],
  [/^You have just created (.+)$/gm, 'Acabas de crear $1'],
  [/^You just removed (.+)$/gm, 'Acabas de eliminar $1'],
  [/^There is no room called (.+)\.$/gm, 'No existe ninguna sala llamada $1.'],
  [/^There is no (.+) here\.$/gm, 'No hay ningún $1 aquí.'],
  [/^New room (.+) created$/gm, 'Nueva sala $1 creada'],
  [/^You just added the (.+) locker$/gm, 'Acabas de añadir el casillero $1'],
  [/^Command '(.+)' not found in room '(.+)'$/gm, "Comando '$1' no encontrado en la sala '$2'."],
  [/^You have correctly entered the password\. You are now in Paradise\.\s*Take a look around, and congratulations\.$/gm,
    'Has introducido la contraseña correctamente. Ya estás en Paradise. Echa un vistazo y enhorabuena.']
];

const BOOK_NOTE = '[Texto original en inglés: estos archivos forman parte del acertijo de grep; ' +
  'busca la línea que contiene la contraseña de sudo.]';

const localizedRooms = new WeakSet();
const localizedItems = new WeakSet();

function translate(text) {
  if (typeof text !== 'string' || text === '') {
    return text;
  }
  const exact = MESSAGES.get(text);
  if (exact !== undefined) {
    return exact;
  }
  const pair = PAIRS.get(text);
  if (pair !== undefined) {
    return pair;
  }
  if (text.length > 900) {
    return text;
  }
  let result = text;
  for (const pattern of PATTERNS) {
    result = result.replace(pattern[0], pattern[1]);
  }
  return result;
}

function isRoom(value) {
  return Boolean(value) && typeof value === 'object' &&
    typeof value.room_name === 'string' &&
    value.cmd_text && Array.isArray(value.items) && Array.isArray(value.children);
}

function isItem(value) {
  return Boolean(value) && typeof value === 'object' &&
    typeof value.itemname === 'string' && value.cmd_text;
}

function localizeItem(item) {
  if (!isItem(item) || localizedItems.has(item)) {
    return;
  }
  localizedItems.add(item);
  for (const command of Object.keys(item.cmd_text)) {
    const value = item.cmd_text[command];
    if (typeof value !== 'string') {
      continue;
    }
    const translated = translate(value);
    if (translated === value && value.length > 900) {
      item.cmd_text[command] = BOOK_NOTE + '\n\n' + value;
    } else {
      item.cmd_text[command] = translated;
    }
  }
}

function localizeRoom(room, visited) {
  if (!isRoom(room) || visited.has(room)) {
    return;
  }
  visited.add(room);
  if (!localizedRooms.has(room)) {
    localizedRooms.add(room);
    if (typeof room.intro_text === 'string') {
      room.intro_text = translate(room.intro_text);
    }
  }
  for (const command of Object.keys(room.cmd_text)) {
    if (typeof room.cmd_text[command] === 'string') {
      room.cmd_text[command] = translate(room.cmd_text[command]);
    }
  }
  for (const item of room.items) {
    localizeItem(item);
  }
  for (const child of room.children) {
    localizeRoom(child, visited);
  }
}

function localizeGame(sandbox) {
  if (!sandbox) {
    return;
  }
  const manPages = sandbox.man_pages;
  if (manPages) {
    for (const command of Object.keys(manPages)) {
      manPages[command] = translate(manPages[command]);
    }
  }
  const visited = new WeakSet();
  for (const key of Object.keys(sandbox)) {
    const value = sandbox[key];
    if (isRoom(value)) {
      localizeRoom(value, visited);
    } else if (isItem(value)) {
      localizeItem(value);
    }
  }
}

function installHooks(sandbox) {
  if (!sandbox) {
    return;
  }
  const Room = sandbox.Room;
  if (typeof Room === 'function' && Room.prototype && !Room.prototype.__terminusEs) {
    const changeIntroText = Room.prototype.changeIntroText;
    const addCmdText = Room.prototype.addCmdText;
    if (typeof changeIntroText === 'function') {
      Room.prototype.changeIntroText = function (text) {
        return changeIntroText.call(this, translate(text));
      };
    }
    if (typeof addCmdText === 'function') {
      Room.prototype.addCmdText = function (command, text) {
        return addCmdText.call(this, command, translate(text));
      };
    }
    Room.prototype.__terminusEs = true;
  }
  const Item = sandbox.Item;
  if (typeof Item === 'function' && Item.prototype && !Item.prototype.__terminusEs) {
    const addCmdText = Item.prototype.addCmdText;
    if (typeof addCmdText === 'function') {
      Item.prototype.addCmdText = function (command, text) {
        return addCmdText.call(this, command, translate(text));
      };
    }
    Item.prototype.__terminusEs = true;
  }
}

module.exports = {
  translate,
  localizeGame,
  installHooks
};
