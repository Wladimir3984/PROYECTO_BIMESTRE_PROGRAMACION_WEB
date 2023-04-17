
INSERT INTO app_categoria(NOMBRE) VALUES('AVENTURA');
INSERT INTO app_categoria(NOMBRE) VALUES('GUERRA');
INSERT INTO app_categoria(NOMBRE) VALUES('PLATAFORMA');
INSERT INTO app_categoria(NOMBRE) VALUES('TERROR');
INSERT INTO app_categoria(NOMBRE) VALUES('RPG');

INSERT INTO app_metodopago(NOMBRE) VALUES('DEBITO');
INSERT INTO app_metodopago(NOMBRE) VALUES('CREDTIO');
INSERT INTO app_metodopago(NOMBRE) VALUES('TRANSFERENCIA');

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id)
VALUES('World of warcraft', 5990, 159, 'World of Warcraft es un videojuego de rol multijugador masivo en linea desarrollado por Blizzard Entertainment. Es el cuarto juego lanzado establecido en el universo fantastico de Warcraft, el cual fue introducido por primera vez por Warcraft: Orcs y Humans en 1994.',5);

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id)
VALUES('Warzone 2.0', 12990, 690, 'Call of Duty: Warzone 2.0 es un videojuego de Battle Royale gratuito que se lanzo para PlayStation 4, PlayStation 5, Xbox One, Microsoft Windows y Xbox Series X|S. Es una secuela de Call of Duty: Warzone de 2020.',2);

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id)
VALUES('Residen evil 4 Remake', 32990, 123, 'Resident Evil 4 cuyo titulo original en Japon es Biohazard 4. Es un videojuego de accion aventura de disparos en tercera persona perteneciente al subgenero de terror y supervivencia desarrollado por Capcom y estrenado el 24 de marzo del 2023.',4);

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id)
VALUES('Hollow knight', 8300, 1543, 'Hollow Knight, desarrollado por Team Cherry, ofrecera una aventura de estilo bidimensional que combinara accion y plataformas en un mundo de fantasia medieval, el reino de Hallownest. Incluira animaciones hechas con estilo tradicional, retos para el jugador, coleccionables por desbloquear y una banda sonora unica.',3);

INSERT INTO app_juego (nombre, precio_venta, stock, descripcion, id_categoria_id)
VALUES('Hogwarts legacy', 39990, 467, 'Hogwarts Legacy es un RPG de accion en un mundo abierto ambientado en el universo de los libros de Harry Potter. Embarcate en un viaje que te llevara a lugares nuevos y ya conocidos, y en el que podras descubrir animales fantasticos, personalizar a tu personaje, elaborar pociones, dominar hechizos, mejorar tus habilidades y convertirte en la bruja o el mago que quieras ser.',1);

COMMIT;