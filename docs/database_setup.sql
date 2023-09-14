create database pybooking;

use pybooking;

create table users(
	id int primary key auto_increment,
	name varchar(50) not null,
	email varchar(50) not null unique,
	password varchar(110) not null
);

create table hotels(
	id int primary key auto_increment,
    name varchar(50) not null,
    location varchar(50) not null,
    daily_rate decimal(8,2) not null,
    rating decimal(2,1) check (rating >= 0.0 and rating <= 5.0) not null,
    additional_info varchar(100) null
);

create table bookings(
	id int primary key auto_increment,
    id_user int not null,
    id_hotel int not null,
    check_in datetime not null,
    check_out datetime not null,
    num_of_adults int check (num_of_adults >= 1) not null,
    num_of_children int check (num_of_children >= 0) not null,
    constraint fk_bookings_id_user foreign key (id_user) references users(id),
    constraint fk_bookings_id_hotel foreign key (id_hotel) references hotels(id)
);
