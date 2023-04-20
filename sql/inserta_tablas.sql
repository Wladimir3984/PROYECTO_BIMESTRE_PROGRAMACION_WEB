INSERT INTO app_categoria(NOMBRE) VALUES('AVENTURA');
INSERT INTO app_categoria(NOMBRE) VALUES('GUERRA');
INSERT INTO app_categoria(NOMBRE) VALUES('PLATAFORMA');
INSERT INTO app_categoria(NOMBRE) VALUES('TERROR');
INSERT INTO app_categoria(NOMBRE) VALUES('RPG');

INSERT INTO app_metodopago(NOMBRE) VALUES('DEBITO');
INSERT INTO app_metodopago(NOMBRE) VALUES('CREDTIO');
INSERT INTO app_metodopago(NOMBRE) VALUES('TRANSFERENCIA');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('World of warcraft', 5990, 159, 'World of Warcraft es un videojuego de rol multijugador masivo en linea desarrollado por Blizzard Entertainment. Es el cuarto juego lanzado establecido en el universo fantastico de Warcraft, el cual fue introducido por primera vez por Warcraft: Orcs y Humans en 1994.',5, 'juegos/RPG/wow.jpg');


INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Residen evil 4 Remake', 32990, 123, 'Resident Evil 4 cuyo titulo original en Japon es Biohazard 4. Es un videojuego de accion aventura de disparos en tercera persona perteneciente al subgenero de terror y supervivencia desarrollado por Capcom y estrenado el 24 de marzo del 2023.',4, 'juegos/TERROR/re4.jpg');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Hollow knight', 8300, 1543, 'Hollow Knight, desarrollado por Team Cherry, ofrecera una aventura de estilo bidimensional que combinara accion y plataformas en un mundo de fantasia medieval, el reino de Hallownest. Incluira animaciones hechas con estilo tradicional, retos para el jugador, coleccionables por desbloquear y una banda sonora unica.',3,
'juegos/PLATAFORMA/hollow.jpg');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Hogwarts legacy', 39990, 467, 'Hogwarts Legacy es un RPG de accion en un mundo abierto ambientado en el universo de los libros de Harry Potter. Embarcate en un viaje que te llevara a lugares nuevos y ya conocidos, y en el que podras descubrir animales fantasticos, personalizar a tu personaje, elaborar pociones, dominar hechizos, mejorar tus habilidades y convertirte en la bruja o el mago que quieras ser.',1, 'juegos/AVENTURA/hogLeg.jpg');

-- Guerra

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Warzone 2.0', 12990, 690, 'Call of Duty: Warzone 2.0 es un videojuego de Battle Royale gratuito que se lanzo para PlayStation 4, PlayStation 5, Xbox One, Microsoft Windows y Xbox Series X|S. Es una secuela de Call of Duty: Warzone de 2020.',2,
'juegos/GUERRA/warzone.jpg');


INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('BatteField 3', 6990, 180, 'La franquicia Battlefield es una serie de videojuegos de disparos en primera persona, de estilo bélico, desarrollada principalmente por EA Digital Illusion CE y distribuida por Electronic Arts.',2,
'juegos/GUERRA/btf.jpg');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Sniper Elite', 2990, 50, 'Sniper Elite es una serie de videojuegos de disparos tácticos desarrollada por Rebellion Developments. Es un juego de disparos táctico en tercera persona que enfatiza un enfoque menos directo del combate, alentando al jugador como francotirador a usar el sigilo y mantenerse alejado de los soldados enemigos.',2,
'juegos/GUERRA/snp.jpg');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id, imagen)
VALUES('Medalla de honor', 5990, 352, 'Medal of Honor es una serie de videojuegos creada y producida por Steven Spielberg. La temática de la serie siempre ha estado basada en los combates de la Segunda Guerra Mundial, tema de culto para Spielberg.',2,
'juegos/GUERRA/moh.jpg');

COMMIT;
