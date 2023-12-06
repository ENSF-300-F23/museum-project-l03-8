-- Create the database
DROP DATABASE IF EXISTS ARTMUSEUM;
CREATE DATABASE ARTMUSEUM;
USE ARTMUSEUM;


CREATE TABLE ARTIST (
    Name VARCHAR(255) PRIMARY KEY,
    DateBorn DATE,
    Date_died DATE,
    Country_of_origin VARCHAR(255),
    Epoch VARCHAR(255),
    Main_style VARCHAR(255),
    Description TEXT
);

CREATE TABLE COLLECTION (
    Name VARCHAR(255) PRIMARY KEY,
    Type VARCHAR(255),
    Description TEXT,
    Address VARCHAR(255),
    Phone VARCHAR(20),
    Contact_person VARCHAR(255)
);

CREATE TABLE EXHIBITION (
    Name VARCHAR(255) PRIMARY KEY,
    Start_date DATE,
    End_date DATE
);

CREATE TABLE ART_OBJECT (
    Id_no INT PRIMARY KEY,
    Artist VARCHAR(255),
    Year INT,
    Title VARCHAR(255),
    Description TEXT,
    Country_of_Origin VARCHAR(255),
    Epoch VARCHAR(255),
    Exhibition VARCHAR(255),
    FOREIGN KEY (Artist) REFERENCES ARTIST(Name),
    FOREIGN KEY (Exhibition) REFERENCES EXHIBITION(Name) ON DELETE CASCADE
);

CREATE TABLE PAINTING (
    Id_no INT PRIMARY KEY,
    Paint_type VARCHAR(255),
    Drawn_on VARCHAR(255),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

CREATE TABLE SCULPTURE (
    Id_no INT PRIMARY KEY,
    Material VARCHAR(255),
    Height INT,
    Weight INT,
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

CREATE TABLE OTHER (
    Id_no INT PRIMARY KEY,
    Type VARCHAR(255),
    Style VARCHAR(255),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

CREATE TABLE PERMANENT_COLLECTION (
    Id_no INT PRIMARY KEY,
    Date_acquired DATE,
    Status VARCHAR(255),
    Cost DECIMAL(10, 2),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);

CREATE TABLE BORROWED (
    Id_no INT PRIMARY KEY,
    Collection_from VARCHAR(255),
    Date_borrowed VARCHAR(55),
    Date_returned VARCHAR(55),
    FOREIGN KEY (Id_no) REFERENCES ART_OBJECT(Id_no)
);
INSERT INTO ARTIST (Name, DateBorn, Date_died, Country_of_origin, Epoch, Main_style, Description)
VALUES
('Hans Holbein the Younger', '1497-01-01', '1543-01-01', 'Germany', 'Renaissance', 'Realistic', 'Considered one of the greatest portraitists of the 16th century'),
('George Gower', '1540-01-01', '1596-01-01', 'England', 'Renaissance', 'Realistic', 'Serjeant Painter to Queen Elizabeth I'),
('Benedetto da Rovezzano', '1474-01-01', '1554-01-01', 'Italy', 'Renaissance', 'Realistic', 'Italian architect and sculptor'),
('John Shute', null, '1563-01-01', 'England', 'Renaissance', 'Realistic', 'English artist and architect'),
('Juan Fernández', null, '1657-01-01', 'Spain', 'Post-Renaissance', 'Realistic', 'Specialized in still life painting'),
('Pablo Picasso', '1881-10-25', '1973-04-08', 'Spain', 'Modern', 'Abstract', 'One of the most influential artists of the 20th century'),
('Isidore Leroy', '1842-01-01', null, 'France', 'Modern', 'Pattern', 'French wallpaper house'),
('Robert Pruitt', '1975-01-01', null, 'American', 'Modern', 'Realistic', 'Known for his figurative drawings'),
('Simone Leigh', '1967-01-01', null, 'American', 'Modern', 'Abstract', 'American artist concerned with the marginalization of women of color'),
('Theaster Gates', '1973-01-01', null, 'American', 'Modern', 'Abstract', 'American social practice artist'),
('Woody de Othello', '1991-01-01', null, 'American', 'Modern', 'Abstract', 'American ceramicist and painter'),
('Robert Campin', '1375-01-01', '1444-04-26', 'Netherlands', 'Renaissance', 'Realistic', 'First great master of Early Netherlandish painting'),
('Anonymous', null, null, null, null, null, 'Used when the artist could not be identified.'),
('Antoine-Louis Barye', '1795-09-24', '1875-06-25', 'France', 'Modern', 'Realistic', 'Famous for his work as an animalier');

INSERT INTO COLLECTION (Name, Type, Description, Address, Phone, Contact_person)
VALUES
('The Met Fifth Avenue', 'Museum', 'The Metropolitan Museum of Art collects, studies, conserves, and presents significant works of art across time and cultures in order to connect all people to creativity, knowledge, ideas, and one another.', '1000 Fifth Avenue, New York, NY, 10028', '212-535-7710', null),
('France', 'Country', 'Owned by the country.', null, null, null),
('National Museums Recovery', 'Recovery', 'A French state organization that manages the looted artworks recovered from Nazi Germany and returned to France after the Second World War.', null, null, null);

INSERT INTO EXHIBITION (Name, Start_date, End_date)
VALUES
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08'),
('Cubism and the Trompe l''Oeil Tradition', '2022-10-20', '2023-01-22'),
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05'),
('''MNR'' Works At The Musée du Louvre', null, null),
('Masterpieces of The Louvre', null, null);

INSERT INTO ART_OBJECT (Id_no, Artist, Year, Title, Description, Country_of_Origin, Epoch, Exhibition)
VALUES
('0001', 'Hans Holbein the Younger', '1537', 'Henry VIII', 'Portrait of Henry VIII', 'England', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0002', 'George Gower', '1567', 'Elizabeth I (The Hampden Portrait)', 'Portrait of Elizabeth I', 'England', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0003', 'Benedetto da Rovezzano', '1524', 'Angel Bearing Candlestick', 'An angel bearing a candlestick', 'Italy', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0004', 'Benedetto da Rovezzano', '1500', 'Candelabrum', 'A candelabrum', 'Italy', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0005', 'Hans Holbein the Younger', '1533', 'Anne Boleyn', 'Portrait of Anne Boleyn', 'England', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0006', 'John Shute', '1563', 'The First and Chief Groundes of Architecture Used in All the Auncient and Famous Monymentes...', 'Written Text', 'England', 'Renaissance', 'The Tudors: Art and Majesty in Renaissance England'),
('0007', 'Juan Fernández', '1636', 'Still Life with Four Bunches of Grapes', 'Still-life painting emerged in the 1600s as a fully independent subject in European art, and grapes and curtains became popular motifs for artists aiming to vaunt their skills', 'Spain', 'Post-Renaissance', 'Cubism and the Trompe l''Oeil Tradition'),
('0008', 'Pablo Picasso', '1912', 'Still Life with Chair Caning', 'Machine-printed to look like the textured rattan weave used in chairs, this piece of trumpery is materially real but patently fake.', 'Spain', 'Modern', 'Cubism and the Trompe l''Oeil Tradition'),
('0009', 'Pablo Picasso', '1914', 'The Absinthe Glass', 'Picasso''s life-size rendering of a glass of alcohol was shocking for its banality.', 'Spanish', 'Modern', 'Cubism and the Trompe l''Oeil Tradition'),
('0010', 'Isidore Leroy', '1908', 'Wallpaper: pattern 15292 R', 'The wallpapers and borders displayed here are similar or identical to those the Cubists used in their collages and pastiched in their paintings.', 'France', 'Modern', 'Cubism and the Trompe l''Oeil Tradition'),
('0011', 'Robert Pruitt', '2019', 'Birth and Rebirth and Rebirth', 'Painting of woman', 'American', 'Modern', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('0012', 'Simone Leigh', '2019', '108 (Face Jug Series)', 'Abstract painting of woman on mug', 'American', 'Modern', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('0013', 'Simone Leigh', '2021', 'Large Jug', 'Abstract mug', 'American', 'Modern', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('0014', 'Theaster Gates', '2020', 'Signature Study', 'Stoneware', 'American', 'Modern', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('0015', 'Woody de Othello', '2021', 'Applying Pressure', 'Vase on Table', 'American', 'Modern', 'Hear Me Now: The Black Potters of Old Edgefield, South Carolina'),
('0016', 'Robert Campin', '1400', 'Vierge et Enfant', 'Virgin and Child', 'Netherlands', 'Renaissance', '''MNR'' Works At The Musée du Louvre'),
('0017', 'Anonymous', '1900', 'Velours à losanges frappés à dominante rouge', 'Velvet with red diamonds', 'Unknown', 'Modern', '''MNR'' Works At The Musée du Louvre'),
('0018', 'Anonymous', '1500', 'Vase hispano-mauresque à quatre anses', 'Hispano-Moorish vase with four handles', 'Spain', 'Renaissance', '''MNR'' Works At The Musée du Louvre'),
('0019', 'Anonymous', '525', 'Feuillet de diptyque en cinq parties : l''Empereur triomphant (Justinien?)', 'Diptych folio in five parts: the triumphant Emperor (Justinian?)', 'Constantinople', 'Middle Ages', 'Masterpieces of The Louvre'),
('0020', 'Anonymous', '100', 'portrait de momie ; L''Européenne', 'Portrait of a Mummy', 'Egypt', 'Roman Period', 'Masterpieces of The Louvre'),
('0021', 'Antoine-Louis Barye', '1832', 'Lion au serpent', 'Lion with a snake', 'France', 'Modern', 'Masterpieces of The Louvre');


INSERT INTO PAINTING (Id_no, Paint_type, Drawn_on)
VALUES
('0001', 'Oil', 'Panel'),
('0002', 'Oil', 'Canvas'),
('0007', 'Oil', 'Canvas'),
('0008', 'Oil', 'Oilcloth'),
('0011', 'Conte', null),
('0016', null, 'Metal'),
('0020', 'Leaf Gliding', 'Cedar');

INSERT INTO SCULPTURE (Id_no, Material, Height, Weight)
VALUES
('0003', 'Bronze', 101, 141),
('0004', 'Bronze', 340, 622),
('0009', 'Bronze', 22.5, null),
('0012', 'Porcelain', 44.5, null),
('0013', 'Stoneware', 158.8, 346.5),
('0014', 'Stoneware', 54.9, 40.8),
('0015', 'Ceramic/Oak Wood', 96.5, null),
('0018', 'Ceramic', 48, null),
('0021', 'Bronze', 135, null);

INSERT INTO OTHER (Id_no, Type, Style)
VALUES
('0005', 'Sketch', 'Realistic'),
('0006', 'Text', 'Written'),
('0010', 'Wallpaper', 'Pattern'),
('0017', 'Textile', 'Pattern'),
('0019', 'Diptych Sheet', 'Realistic');

INSERT INTO PERMANENT_COLLECTION (Id_no, Date_acquired, Status, Cost)
VALUES
('0001', null, 'On Display', null),
('0002', null, 'On Display', null),
('0003', null, 'On Display', null),
('0004', null, 'On Display', null),
('0005', null, 'On Display', null),
('0006', null, 'On Display', null),
('0007', null, 'On Display', null),
('0008', null, 'On Display', null),
('0009', null, 'On Display', null),
('0010', null, 'On Display', null),
('0011', null, 'On Display', null),
('0012', null, 'On Display', null),
('0013', null, 'On Display', null),
('0014', null, 'On Display', null),
('0015', null, 'On Display', null);

INSERT INTO BORROWED (Id_no, Collection_from, Date_borrowed, Date_returned)
VALUES
('0016','National Museums Recovery','1950', null),
('0017','National Museums Recovery','1951', null),
('0018','National Museums Recovery','1999', null),
('0019','France','1899', null),
('0020','France','1951', null),
('0021','France','March 28, 1911', null);