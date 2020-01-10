drop table if exists user;
create table user (
  id text primary key,
  username text not null,
  email text not null
);