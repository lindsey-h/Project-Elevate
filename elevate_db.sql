--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2 (Ubuntu 13.2-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.2 (Ubuntu 13.2-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contacts; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.contacts (
    contact_id integer NOT NULL,
    user_id integer NOT NULL,
    fname character varying NOT NULL,
    lname character varying NOT NULL,
    email character varying NOT NULL,
    phone_number character varying NOT NULL
);


ALTER TABLE public.contacts OWNER TO hackbright;

--
-- Name: contacts_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.contacts_contact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.contacts_contact_id_seq OWNER TO hackbright;

--
-- Name: contacts_contact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.contacts_contact_id_seq OWNED BY public.contacts.contact_id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.events (
    event_id integer NOT NULL,
    title character varying NOT NULL,
    date timestamp without time zone NOT NULL,
    description text,
    duration_in_minutes integer,
    is_available boolean NOT NULL
);


ALTER TABLE public.events OWNER TO hackbright;

--
-- Name: events_event_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.events_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_event_id_seq OWNER TO hackbright;

--
-- Name: events_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.events_event_id_seq OWNED BY public.events.event_id;


--
-- Name: photos; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.photos (
    photo_id integer NOT NULL,
    url character varying NOT NULL,
    animal_type character varying NOT NULL
);


ALTER TABLE public.photos OWNER TO hackbright;

--
-- Name: photos_photo_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.photos_photo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.photos_photo_id_seq OWNER TO hackbright;

--
-- Name: photos_photo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.photos_photo_id_seq OWNED BY public.photos.photo_id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.posts (
    post_id integer NOT NULL,
    user_id integer NOT NULL,
    text character varying NOT NULL,
    date timestamp without time zone NOT NULL
);


ALTER TABLE public.posts OWNER TO hackbright;

--
-- Name: posts_post_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.posts_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_post_id_seq OWNER TO hackbright;

--
-- Name: posts_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.posts_post_id_seq OWNED BY public.posts.post_id;


--
-- Name: quotes; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.quotes (
    quote_id integer NOT NULL,
    text character varying NOT NULL,
    author character varying NOT NULL
);


ALTER TABLE public.quotes OWNER TO hackbright;

--
-- Name: quotes_quote_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.quotes_quote_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.quotes_quote_id_seq OWNER TO hackbright;

--
-- Name: quotes_quote_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.quotes_quote_id_seq OWNED BY public.quotes.quote_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    fname character varying NOT NULL,
    lname character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.users OWNER TO hackbright;

--
-- Name: users_events; Type: TABLE; Schema: public; Owner: hackbright
--

CREATE TABLE public.users_events (
    user_event_id integer NOT NULL,
    user_id integer NOT NULL,
    event_id integer
);


ALTER TABLE public.users_events OWNER TO hackbright;

--
-- Name: users_events_user_event_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.users_events_user_event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_events_user_event_id_seq OWNER TO hackbright;

--
-- Name: users_events_user_event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.users_events_user_event_id_seq OWNED BY public.users_events.user_event_id;


--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: hackbright
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO hackbright;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hackbright
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: contacts contact_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.contacts ALTER COLUMN contact_id SET DEFAULT nextval('public.contacts_contact_id_seq'::regclass);


--
-- Name: events event_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.events ALTER COLUMN event_id SET DEFAULT nextval('public.events_event_id_seq'::regclass);


--
-- Name: photos photo_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.photos ALTER COLUMN photo_id SET DEFAULT nextval('public.photos_photo_id_seq'::regclass);


--
-- Name: posts post_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.posts ALTER COLUMN post_id SET DEFAULT nextval('public.posts_post_id_seq'::regclass);


--
-- Name: quotes quote_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.quotes ALTER COLUMN quote_id SET DEFAULT nextval('public.quotes_quote_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Name: users_events user_event_id; Type: DEFAULT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users_events ALTER COLUMN user_event_id SET DEFAULT nextval('public.users_events_user_event_id_seq'::regclass);


--
-- Data for Name: contacts; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.contacts (contact_id, user_id, fname, lname, email, phone_number) FROM stdin;
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.events (event_id, title, date, description, duration_in_minutes, is_available) FROM stdin;
1	Arts and Crafts	2021-08-19 21:48:07.692609	\N	60	t
2	Something really fun	2021-08-28 20:07:29.513841	\N	90	t
3	Monkey Business	2021-12-12 17:00:00	\N	60	t
4	Painting	2020-12-12 16:00:00	\N	60	t
5	One thing 	2021-12-12 17:05:00	Or another 	60	t
6	Petting zoo	2021-08-21 10:00:00	Pet cute, furry little animals. Get a large pretzel. 	60	t
7	Puzzles	2021-08-21 16:00:00	Jigsaw puzzles and games	60	t
8	Debugging Session	2021-09-02 17:00:00	This is fun even though it's hard	60	t
9	Kipo the cat	2021-09-04 07:00:00	Never stops meowing at me for no reason	60	t
\.


--
-- Data for Name: photos; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.photos (photo_id, url, animal_type) FROM stdin;
\.


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.posts (post_id, user_id, text, date) FROM stdin;
\.


--
-- Data for Name: quotes; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.quotes (quote_id, text, author) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.users (user_id, fname, lname, email, password) FROM stdin;
1	Pam	Beasley	pbandj@dunder.com	password
2	Jim	Halpert	jimhalps@dunder.com	password
3	Dwight	Schrutte	dwight@dunder.com	password
4	Michael	Scott	worldsbestboss@dunder.com	password
\.


--
-- Data for Name: users_events; Type: TABLE DATA; Schema: public; Owner: hackbright
--

COPY public.users_events (user_event_id, user_id, event_id) FROM stdin;
3	2	1
4	2	7
5	3	6
6	3	7
7	3	9
8	3	1
9	3	1
10	3	2
11	3	2
12	3	9
13	3	9
14	3	9
15	3	9
16	3	9
17	3	9
18	3	9
19	3	9
20	3	9
255	1	9
257	1	6
258	4	6
\.


--
-- Name: contacts_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.contacts_contact_id_seq', 1, false);


--
-- Name: events_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.events_event_id_seq', 9, true);


--
-- Name: photos_photo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.photos_photo_id_seq', 1, false);


--
-- Name: posts_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.posts_post_id_seq', 1, false);


--
-- Name: quotes_quote_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.quotes_quote_id_seq', 1, false);


--
-- Name: users_events_user_event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.users_events_user_event_id_seq', 258, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hackbright
--

SELECT pg_catalog.setval('public.users_user_id_seq', 5, true);


--
-- Name: contacts contacts_email_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_email_key UNIQUE (email);


--
-- Name: contacts contacts_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_phone_number_key UNIQUE (phone_number);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (contact_id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (event_id);


--
-- Name: photos photos_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_pkey PRIMARY KEY (photo_id);


--
-- Name: photos photos_url_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.photos
    ADD CONSTRAINT photos_url_key UNIQUE (url);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (post_id);


--
-- Name: quotes quotes_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.quotes
    ADD CONSTRAINT quotes_pkey PRIMARY KEY (quote_id);


--
-- Name: quotes quotes_text_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.quotes
    ADD CONSTRAINT quotes_text_key UNIQUE (text);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users_events users_events_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users_events
    ADD CONSTRAINT users_events_pkey PRIMARY KEY (user_event_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: contacts contacts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: posts posts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: users_events users_events_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users_events
    ADD CONSTRAINT users_events_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- Name: users_events users_events_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hackbright
--

ALTER TABLE ONLY public.users_events
    ADD CONSTRAINT users_events_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

