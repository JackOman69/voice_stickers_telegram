--
-- PostgreSQL database dump
--

-- Dumped from database version 15.1 (Debian 15.1-1.pgdg110+1)
-- Dumped by pg_dump version 15.1 (Debian 15.1-1.pgdg110+1)

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
-- Name: voicestickers; Type: TABLE; Schema: public; Owner: postgres_voicestickers
--

CREATE TABLE public.voicestickers (
    id integer NOT NULL,
    voice character varying(255),
    name character varying(50),
    description text,
    tags text[],
    author character varying(50),
    created_date character varying(50),
    admin_author_id integer
);


ALTER TABLE public.voicestickers OWNER TO postgres_voicestickers;

--
-- Name: voicestickers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres_voicestickers
--

ALTER TABLE public.voicestickers ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.voicestickers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: voicestickers; Type: TABLE DATA; Schema: public; Owner: postgres_voicestickers
--

COPY public.voicestickers (id, voice, name, description, tags, author, created_date, admin_author_id) FROM stdin;
24	AwACAgIAAxkBAAIaAAFjefnWzzBi610pMytR_aDygbCoKAACXxIAAmbneEs4IuhqVsG1nCsE	Абобус	Абооообус	{илья,шиза,крик}	Илья	2022-11-20 09:56:59	458554554
25	AwACAgIAAxkBAAIaDmN5-f5rpkVDaypsTXGWuOt2ov76AAIRDwACHJKISyp48eFxLdsEKwQ	Леша отчисляет шарагу	Леша собирается отчислить шарагу	{леша,классика}	Леша	2022-11-20 09:57:44	458554554
2	AwACAgIAAxkBAAIYS2N58qDpfAWhZnlIFgM__VFKH4lDAAKcCQACd4JxSQ1Th9tysFXcKwQ	Кошечка сказала заебись	Серик воспроизводит старый мем про кошечку	{серик,классика,цитаты}	Серик	2022-11-20 09:27:10	458554554
3	AwACAgIAAxkBAAIYWWN58yXdA3AneBQ7eQdstTftVasWAAKNEAACGDiZS0wh9cFiHxDVKwQ	Я не знаю😭	Серик опять ничего не знает	{серик,классика}	Серик	2022-11-20 09:28:33	458554554
4	AwACAgIAAxkBAAIYamN585UyDNKJa6ZB1sfnDt2snUO9AAKqCwAC8PzBSqgUuBPcSfiwKwQ	Егор ты где есть?	Серик издают шизофренический звук на фоне	{илья,серик,шизозвуки,крики,классика}	Илья	2022-11-20 09:30:56	458554554
5	AwACAgIAAxkBAAIYeGN58-dSvcwwTU0cNCHpNHbraP6xAAJZDgACgTAwS-DpVuO3RrdtKwQ	Где мои биткойны?🤔	Егор опять потерял свои биткойны	{егор,классика}	Егор	2022-11-20 09:31:57	458554554
6	AwACAgIAAxkBAAIYmGN59Eedht47L9qsd_jil9OEYs2UAALkDQAC76lJS_mxZMNbpFZoKwQ	Серик вернулся с завода	Серик вернулся с завода	{серик,классика}	Серик	2022-11-20 09:33:23	458554554
7	AwACAgIAAxkBAAIYpmN59HU2WEOg9Qu4N1ydxpICD0bGAALoDwACiG9hS-kI9z8iiqzFKwQ	Я соска нереалка	У Ильи всплеск гормонов и он снова соска нереалка	{илья,шиза}	Илья	2022-11-20 09:34:31	458554554
8	AwACAgIAAxkBAAIYtGN59LidO-LdIfVpoxpTRsNIa08BAAJwEgACFxVQSN41pXCBwIJSKwQ	🎙Солевой радиоприемник🎙	Солевой радиоприемник, кхкхкхк	{леша,шиза,классика}	Леша	2022-11-20 09:35:36	458554554
9	AwACAgIAAxkBAAIYwmN59PghNrdnfG0gg4TBNtfb4H1gAAJHAwACwX4RSdQBgNOfBVpzKwQ	Я тебе сломаю, мозг и шею	Леша ругается, очень громко	{леша,ругательства,крики}	Леша	2022-11-20 09:36:37	458554554
10	AwACAgIAAxkBAAIY0GN59TuKDloudAaWCZz3l6luHkSnAAIlBgACLf0xShrHQUTQJgVVKwQ	Я тут двери выбиваю	Егор выбивает двери	{егор,классика}	Егор	2022-11-20 09:37:17	458554554
11	AwACAgIAAxkBAAIY3mN59Xw3roFqqBVE2C_OsBbou-8YAAJWEgACkuApSfoKIfGCy8cGKwQ	Бобры не спят	Исполнение какой-то шизо песни от Серика	{серик,шиза,классика}	Серик	2022-11-20 09:38:37	458554554
12	AwACAgIAAxkBAAIY7GN59a4LoRbNYU-RCa-ZYuYlwxjcAALEEAAC_SzBST2ncL-EKXFqKwQ	Я так рад!😄	Серик очень рад	{серик,классика}	Серик	2022-11-20 09:39:27	458554554
13	AwACAgIAAxkBAAIY-mN59mK2qMmH7QItMkk-2PHO7_HDAAKhDwACvWTISUNQKtOkuGu2KwQ	Криминальному криминалу	Снова криминал	{илья,шиза,классика}	Илья	2022-11-20 09:42:40	458554554
14	AwACAgIAAxkBAAIZCGN59q7ZEtRfMMDwzPQOHpSQSr-cAAKzEgAC9JhBSopf4rpuSfZ6KwQ	ПОСОСИ💋	Пососи	{илья,ругательства}	Илья	2022-11-20 09:43:40	458554554
15	AwACAgIAAxkBAAIZFmN59t4xqi-bWrX1JYk2N88KHIk-AALMFAACvjg5SvP4JB6Wa30mKwQ	Егор стал быдло	Егор ну как и был быдло так и стал им	{серик,ругательства,классика}	Серик	2022-11-20 09:44:30	458554554
16	AwACAgIAAxkBAAIZJGN59wtTaGAs29Yo9lJokiiPtwKuAALYEQAC89xYSomS_8frqT4VKwQ	Игнорирую	Игнорирую нехороших людей	{илья,ругательства,крики}	Илья	2022-11-20 09:45:06	458554554
17	AwACAgIAAxkBAAIZMmN59y-hzop3VtiPdXIbFKzN7D3mAALEDwACSsN5SlqwyCbWMfU3KwQ	Срать охота крепкое	Егор снова какает...	{егор,классика}	Егор	2022-11-20 09:45:40	458554554
18	AwACAgIAAxkBAAIZbGN598qzgXrrppYNojGE8IUsA2EeAAK4EgACZ3PgSmqz1El5uo7GKwQ	Егор пошел куда-то	Серик опять ругается на больного	{серик,ругательства,крик}	Серик	2022-11-20 09:48:18	458554554
26	AwACAgIAAxkBAAIaHGN5-izNc3oZKMw5oTrAuZ4jNk1WAAKJDwACa56wS86zKdrr4N9gKwQ	Олег Тинькофф	К Леше пришел Олег Тинькофф	{леша,шиза,классика}	Леша	2022-11-20 09:58:28	458554554
20	AwACAgIAAxkBAAIZqmN5-LxDCliAXX4v5UPvawG1Q-4QAAJ5DgACeqP5Ss_Q2oHcQrhkKwQ	Илья, где деньги?	Егор опять просит денег	{егор,ругательства,крик}	Егор	2022-11-20 09:52:23	458554554
21	AwACAgIAAxkBAAIZumN5-OrteJK4dq5h2Zlg3PYHew_PAAL-EQACetbZSsaqzyUxY_YhKwQ	Серик уже готов	Серик уже у подьезда и готовиться принимать	{серик,геи}	Серик	2022-11-20 09:53:07	458554554
22	AwACAgIAAxkBAAIZ1mN5-UmN1blJ9eeBc_CheLc5qDseAALmEQACp-twS35vy7NA3ZzHKwQ	Логики нет	Серик как всегда не нашел логику	{серик,классика}	Серик	2022-11-20 09:54:38	458554554
23	AwACAgIAAxkBAAIZ8mN5-adaTm4g8FhmstdWwq6QhV3oAAKZEQACx1R4S_xEAAGOmmXV-isE	Рвет панцирь	У Леши как всегда рвет поддон	{леша,классика}	Леша	2022-11-20 09:56:20	458554554
27	AwACAgIAAxkBAAIaKmN5-l7DeVF3Yv8mqDtygGbyHliVAAJlEQACcBbBS2O_AUE11bL5KwQ	Вот шо ты наделал!?	Вот опять шо-то кто-то наделал	{леша,классика}	Леша	2022-11-20 09:59:27	458554554
28	AwACAgIAAxkBAAIaOGN5-pHzGYohvggjCWEYt9Du9bU8AAJmEQACcBbBSwVdw0JrfMDfKwQ	На месте порешаем	Бытовые будни быта	{илья,классика}	Илья	2022-11-20 10:00:16	458554554
29	AwACAgIAAxkBAAIaRmN5-tl6w5fk1KXZkjmK9n03NQWzAAI7FwACob8ZSL9ko7t67QtDKwQ	Егор лох	Егор снова лох	{серик,ругательства,классика}	Серик	2022-11-20 10:01:20	458554554
30	AwACAgIAAxkBAAIaVGN5-vhxyfRe-VZ1SkfGsBWSrY5uAAKpFgAChxEYSDRREJvre9bjKwQ	Абсолютно адекватен	Серик абсолютный адыкватный человек	{серик,классика}	Серик	2022-11-20 10:01:59	458554554
31	AwACAgIAAxkBAAIaYmN5-zNezxI_LK8WoOqgrdawqqVlAAJIDgAChiuBSBcw9w2_-YurKwQ	Хватит игнорить	Егор хватит игнорить	{илья,ругательства,классика}	Илья	2022-11-20 10:02:56	458554554
32	AwACAgIAAxkBAAIacGN5-2IHSVoHtEwO3rD8fK2issnAAALcEAACv6KISKWo6wj_ciyqKwQ	ТЫ БЛЯТЬ ХУЙЛУША	...	{илья,ругательства,классика}	Илья	2022-11-20 10:03:50	458554554
33	AwACAgIAAxkBAAIafmN5-5Cn0MtSHLpzSGd-FiHbu3UJAAJgFAAC_bW4SJL2jnMHR1iCKwQ	Апчхуй	Снова апчхуй	{илья,шизозвуки,классика}	Илья	2022-11-20 10:04:21	458554554
34	AwACAgIAAxkBAAIajGN5-7ROISBP96DzAxf9V5s9laJpAAJ5FAAC97KwSIa0kEZbDpDOKwQ	Классические шизо-звук	Классические шизо-звуки у Леши дома	{леша,шиза,шизозвуки}	Леша	2022-11-20 10:05:22	458554554
35	AwACAgIAAxkBAAIammN5--5-1vkgpvdT6Sqt1DEWpx9BAAJcFAAC_bW4SEZgNGVPaMnKKwQ	Я просто очень занят	Илья очень занят	{илья,классика}	Илья	2022-11-20 10:05:55	458554554
36	AwACAgIAAxkBAAIaqGN5_BG7DG-xQoziG-qL2nM1_v5nAAJ3FgAC7UJ4SfENh1cBCJAmKwQ	Леша едет куда надо	Леша едет...	{леша,геи}	Леша	2022-11-20 10:06:34	458554554
37	AwACAgIAAxkBAAIatmN5_DxX60l9N-ygj7OdgiW-JW2sAAKHFQACDAbRSd77LeDlDA9KKwQ	Ебаааный	Исполнение Серика песни ебанный бисвап	{серик,классика,ругательства}	Серик	2022-11-20 10:07:27	458554554
38	AwACAgIAAxkBAAIaxGN5_Gs2s76S1NHzdmyzWV9DK55jAAKvFQACCEoRSgIu4Gz-Qa4VKwQ	привет меня зовут даня	привет меня зовут даня	{леша,шизозвуки}	Леша	2022-11-20 10:07:58	458554554
39	AwACAgIAAxkBAAIa0mN5_JwXgPV8IfCV6xIqwGzB_Dp3AAJMEwACBjPISxQ0W6JrWBy-KwQ	Яйца сгорают	У Леши ничего нового и у него сгорают яйца	{леша,шиза,классика}	Леша	2022-11-20 10:08:52	458554554
40	AwACAgIAAxkBAAIa4GN5_Mx4QpHreAbzpjhMFJ-yYvhEAAJbEwACBjPIS3EcLgWOQbVuKwQ	Гений высшего сорта	Леша задумался	{леша,шиза,классика}	Леша	2022-11-20 10:09:37	458554554
41	AwACAgIAAxkBAAIa7mN5_PVwvfAyE5X4xanAZ20HTcvZAAK8FQACZMkJSPussyiMHXmrKwQ	Боевой клич	Леша издает боевой клич всех алкошариков	{леша,классика}	Леша	2022-11-20 10:10:39	458554554
42	AwACAgIAAxkBAAIa_GN5_Sz39ZKCMs0e6s5s3LN7I1EeAAKLFQAC-3UZSOqXpcPF4I44KwQ	Эти геи - геи	Эти геи очень геи	{леша,геи}	Леша	2022-11-20 10:11:13	458554554
43	AwACAgIAAxkBAAIbCmN5_UqqqCGskGFHkQuwiaTXnYRLAAL4FQACtqMoSNzMNpRPqFvzKwQ	Хуявей	Илья хочет хуявей	{илья,шизозвуки}	Илья	2022-11-20 10:11:45	458554554
44	AwACAgIAAxkBAAIbGGN5_XYQqoSELC32vTZQ5k3pAhe5AAI-FwACxy1RSDSUavod1UKjKwQ	Блэээ	...	{илья,крик,шизозвуки}	Илья	2022-11-20 10:12:27	458554554
45	AwACAgIAAxkBAAIbJmN5_ZJmWzN9cjA38qfQStdgYilBAAJ_FAACuQlYSOu7yX79u7vSKwQ	аааа	ААААА	{леша,крик}	Леша	2022-11-20 10:12:50	458554554
46	AwACAgIAAxkBAAIbNGN5_a-CFcInRMzmZ_kmSaUhIpjpAALmFAACSWloSFqILo7qP75iKwQ	Очень смешно	Очень смешно, прямо оборжаться	{илья,классика}	Илья	2022-11-20 10:13:27	458554554
47	AwACAgIAAxkBAAIbQmN5_diyTgABl791xaGrRazxBX9rOwACbRkAAltPeUg3djETsnXzLisE	Начинайте без меня	Не ждите начинайте без меня	{илья,классика}	Илья	2022-11-20 10:14:07	458554554
48	AwACAgIAAxkBAAIbUGN5_gfzhfx5sxivRWEj2RQ0GtzvAAJ0GwAC0nnBSCRuFlnwb1TCKwQ	Сопля об дерево	Леша опте соплю об дерево	{леша,классика}	Леша	2022-11-20 10:14:53	458554554
49	AwACAgIAAxkBAAIbXmN5_l5BLrA4i3-K_NPp8MTn8Cp4AAIUFwACfxfhSDjFn8jg-SWjKwQ	Да, это шизофрения	Звуки Егор по ночам и его дела	{леша,шизозвуки}	Леша	2022-11-20 10:16:31	458554554
50	AwACAgIAAxkBAAIbbGN5_uvGvmitde-5CGRddWcdd0AWAAJEHQACRwjhSHB0a7M7Ks-gKwQ	Ты бы мог офвафывап	Илья накурился кальяном	{илья,шизозвуки,шиза}	Илья	2022-11-20 10:18:58	458554554
51	AwACAgIAAxkBAAIbemN5_z7_nWwCYKP7J-3-A19D_rfrAAJWFwACfxfhSAjqvL8lxSMgKwQ	Пельмени, блять пизда	Каша из пельменей в прямом эфире	{леша,шиза}	Леша	2022-11-20 10:20:05	458554554
52	AwACAgIAAxkBAAIbiGN5_2SiiIWCSeDebzOSDg7_ildzAAKmFwACfxfhSA2eTmMt5TtYKwQ	Я хочу какать	Илья снова хочет какать	{илья,классика}	Илья	2022-11-20 10:20:35	458554554
53	AwACAgIAAxkBAAIblmN5_35mF58S3p7ABh4zNcWM7SQYAAKmFgACtTLhSOPcCeoMbTHxKwQ	Интересный факт	Леша выдал интересный факт	{леша,классика,шиза}	Леша	2022-11-20 10:21:09	458554554
54	AwACAgIAAxkBAAIbr2N5_82e3lm99X_vkY_OZEZm5Em9AAJAFwACVn84SWGU1O6rjDpOKwQ	Илюшаа	Леша опять угрожает Илье	{леша,классика}	Леша	2022-11-20 10:22:42	458554554
55	AwACAgIAAxkBAAIbvWN6AAEYzQZ8WA9oZkEaEdXfpGrLNAACRBcAAlZ_OEnI66ItTlZtVysE	Илюююшааа ты где?	Илюша ты где? Уже поехали угрозы	{леша,классика}	Леша	2022-11-20 10:23:42	458554554
56	AwACAgIAAxkBAAIby2N6AAE_lbdDgCzarJslibjhfrYg_wACKxMAAjLYWUkk1HSirYqiZisE	Ведро?	🪣Ведро? АААА	{леша,шизозвуки}	Леша	2022-11-20 10:24:36	458554554
57	AwACAgIAAxkBAAIb2WN6AAFzIZlP9oPWctbx176ZnJw9rgACZhoAAh-jgEmi9LP80ZbkMisE	Я футбольный мячик	Леша футбольный мячик	{леша,классика,цитаты}	Леша	2022-11-20 10:25:11	458554554
58	AwACAgIAAxkBAAIb52N6AAGcJO2_iUFKBaP7QCiqCuwzjgACbBoAAh-jgElPfpwTRJM9vCsE	А?	А?	{леша,шизозвуки}	Леша	2022-11-20 10:25:43	458554554
59	AwACAgIAAxkBAAIb9WN6AAGzaqr5AaJQ_bCXtcA4row7OgAChxwAAh-jiElgpM7QcQnb8CsE	Вот это ты конечно выдал!	Леша в шоке, потому что кто-то выдал	{леша,шиза,классика}	Леша	2022-11-20 10:26:27	458554554
60	AwACAgIAAxkBAAIcA2N6AAHuOnDpF1NyuHqt7CuOz9idEwAC8xwAAh-jiEmP92_UXhM66CsE	Иногда хочется	Иногда хочется	{леша,шиза,классика}	Леша	2022-11-20 10:27:10	458554554
61	AwACAgIAAxkBAAIcEWN6ARZ7zbEf0Z06w0jLG0LwSsZQAAI5FwACw2rgSSl-Gc3Cs1h2KwQ	Ауф цитата	Леша заговорил ауф цитатами	{леша,классика,цитаты}	Леша	2022-11-20 10:28:00	458554554
62	AwACAgIAAxkBAAIcH2N6AUNpm41gX5Y2y8WYavvS5VNvAAJBGgAC00kYSk5SVclRS_bEKwQ	Маршрут до туалета!	Леша опять едет какать	{леша,классика}	Леша	2022-11-20 10:28:40	458554554
63	AwACAgIAAxkBAAIcLWN6AXIrys-gI5nAZx1kk4Odk1FWAALgGAACqaRBSjYi3omlz1THKwQ	Все я все сказал!	Леша все сказал что очень хотел сказать	{леша,классика,шиза}	Леша	2022-11-20 10:29:24	458554554
64	AwACAgIAAxkBAAIcO2N6AZEzhcwHTR65uYPApE-R5LBTAALjGAACqaRBSi4mi5Erda_nKwQ	Серафииим	Леша зазывает самку	{леша,шиза,шизозвуки}	Леша	2022-11-20 10:29:55	458554554
65	AwACAgIAAxkBAAIcSWN6AcpNi0F8009GHHi4pMg5ZfUbAAKQFQACO_15SlLOBUMjkwtkKwQ	Очень громкий чих	Леша опят чхает, аллергик ебобаный	{леша,крик}	Леша	2022-11-20 10:31:03	458554554
66	AwACAgIAAxkBAAIcZWN6Ai6lj7cc8XQDMLwmC73jT5X0AAIwEwAC1mVBS_YwG3ljuaudKwQ	Пидарас	Илья опять ругается	{илья,ругательства}	Илья	2022-11-20 10:32:31	458554554
67	AwACAgIAAxkBAAIcc2N6Akn5qgmOns8C0tUUm0DJXJMeAAKCGwACeZxRSyx_R7DWldXsKwQ	Скинь сиськи э заебал!	Скинь сиськи э заебал, Серик надышался Московой	{серик,ругательства,классика}	Серик	2022-11-20 10:33:13	458554554
68	AwACAgIAAxkBAAIcgWN6AnaTO6raUolRnFkUXMsB2rzXAAKHGwACeZxRS-PFKi8ChGRcKwQ	Эти самые отношения, дон	Серик превращается в коренного Москвича	{серик,классика}	Серик	2022-11-20 10:34:05	458554554
69	AwACAgIAAxkBAAIcj2N6AqcDsCseGt_gCa6kEplexwvpAAJUKwACIWWIS3Mw9ocryccwKwQ	Я подсолнуххх!!!	Глеб накурился грибов и стал огурцом	{глеб,классика}	Глеб	2022-11-20 10:34:46	458554554
70	AwACAgIAAxkBAAIcnWN6At__yUKaLOeHfuoRfH_EYU_wAAJbKwACIWWISwqMMsFzYGRQKwQ	Опять про волшебные грибочки	Глеб опять про волшебные грибочки	{глеб,шиза}	Глеб	2022-11-20 10:35:39	458554554
71	AwACAgIAAxkBAAIcvGN6Ay6wS4UPTaY2Bzgkf4Reu86nAAIFGAACNmGQS_pCYMlwNjWHKwQ	Не пизди!	Илья плювается в телефон	{илья,ругательства,классика}	Илья	2022-11-20 10:36:45	458554554
72	AwACAgIAAxkBAAIcymN6A1HRmdgthkD-AQ4Pj0DB6B3ZAAJHHQACFEapS3z1Eeqv_95iKwQ	Приступ разрывной	Леша словил приступ разрывной	{леша,классика,шиза}	Леша	2022-11-20 10:37:31	458554554
73	AwACAgIAAxkBAAIc2WN6A5xg6SXX0003qdb_eGA_0a4RAAJPHQACFEapSxiNkzQOQZT1KwQ	Кто прослушал это сообщение, тот гей	...	{леша,геи}	Леша	2022-11-20 10:38:46	458554554
74	AwACAgIAAxkBAAIc52N6A78d3Jgg79ntWidbqlnk_n-QAAJyHQACFEapS6eB14HL8LTaKwQ	Скока можно	Скока можно блять!!!	{леша,классика,цитаты}	Леша	2022-11-20 10:39:15	458554554
75	AwACAgIAAxkBAAIc9WN6A9sDWzoX-hed0ZHNQHMv0cJTAALkHQACFEapS5-fTKZXo-F3KwQ	Снова разрывная	...	{леша,классика,цитаты}	Леша	2022-11-20 10:39:45	458554554
76	AwACAgIAAxkBAAIdA2N6BAPCAkG6HkU0G_ks7oJnx_OBAAJQGwACNlvIS44czr1_0CPiKwQ	Куда ты сьебался?	Илья снова пьян и гонит на Серик	{илья,пьянь}	Илья	2022-11-20 10:40:40	458554554
77	AwACAgIAAxkBAAIdEWN6BDJ60dtqklpvrEbsEJCwbGwWAAJSGwACNlvIS8xCNBhR7gABwisE	Почему так нахуй блять	Почему так нахуй блять	{илья,пьянь}	Илья	2022-11-20 10:41:08	458554554
78	AwACAgIAAxkBAAIdH2N6BF-6s2L9mlbTAZmHE5OzIXg3AALRGwACaaEZSGw2TVSf2w5dKwQ	Илья, еб твою налево	Илья еб твою налево я щас тебе по голове настучу	{егор,ругательства}	Егор	2022-11-20 10:42:04	458554554
79	AwACAgIAAxkBAAIdLWN6BJLpd8xNlt3KtCA6lTNu4rsMAALTGwACaaEZSEKzAt92ZbiIKwQ	Никуда я не пойду	Егор сам себя обманыет	{егор,классика}	Егор	2022-11-20 10:42:42	458554554
80	AwACAgIAAxkBAAIdO2N6BK6IZdwwHGAaG1RpGRWYJ0klAAIuGwACV0chSIgomxa1gGtMKwQ	Давай буль меня	Глебя снова булят	{глеб,ругательства,классика}	Глеб	2022-11-20 10:43:12	458554554
81	AwACAgIAAxkBAAIdSWN6BM8dqjEAAam89Hve31og7jUitQAC9BYAAqvMUUixrqfuOMDJWSsE	Шуриповерта у меня нет	...	{илья,классика}	Илья	2022-11-20 10:43:46	458554554
82	AwACAgIAAxkBAAIdV2N6BQGQb09_OXEJBPhA8ataqvTMAAJLHQAC3k9oSPR_0k-276fLKwQ	Эрен умрет	У Леши снова шиза что все умрут	{леша,классика,шиза}	Леша	2022-11-20 10:44:39	458554554
83	AwACAgIAAxkBAAIdZWN6BT5SjrwbJ3EpbxG0EeaLF2jYAAL3HgACCRyJSJI31DGmP7WyKwQ	Мусьегандонье	...	{илья,ругательства}	Илья	2022-11-20 10:45:34	458554554
87	AwACAgIAAxkBAAIduGN6BnNra6L7uXuJI6hq2QG4SPOJAAINGQAChjrwSLkfsud1xZRHKwQ	Я тебя очень сильно люблю	Серик опять любит	{серик,цитаты}	Серик	2022-11-20 10:50:54	458554554
85	AwACAgIAAxkBAAIdnGN6BhF4aoAPz5H21xx8VVblnRg-AALTGQAC3VmxSEfVqSsL4KmVKwQ	Волчатки	Серик едет к своим волчатка	{серик,классика}	Серик	2022-11-20 10:49:07	458554554
86	AwACAgIAAxkBAAIdqmN6BktaM-GTi7h8bEl8w5h2KIQXAAIiGgACzF3ASAnQaYpPluWrKwQ	Все очень просто	...	{илья,классика,цитаты}	Илья	2022-11-20 10:50:09	458554554
88	AwACAgIAAxkBAAIdxmN6BqzZ4yOslVTyaSIzUv_WgCR-AAJtHwACinUhSRV8-i-zhYFOKwQ	Поцелуй	Серик чмокает тебя через экран	{серик,классика}	Серик	2022-11-20 10:51:41	458554554
89	AwACAgIAAxkBAAId1GN6BwzZHqyYH6XyWRkNUMGBvoRcAAKWGQAC-TpZSqy-RWngcI57KwQ	Мем про платину	...	{егор,цитаты}	Егор	2022-11-20 10:53:51	458554554
90	AwACAgIAAxkBAAId4mN6B2xlb0krIwvk37nkSJtaB0taAAJyGgACPPdJS2OFuqKodEEWKwQ	Карбюратору пизда	Карбулятору снова пизда и Илью шизит	{илья,шиза,классика}	Илья	2022-11-20 10:55:00	458554554
91	AwACAgIAAxkBAAId8GN6B5d66ie1NZWaab9-UrI4yaxdAAL0IQACYAqgSJZckMj7eBA6KwQ	Сладких снов	Леша желает всем сладких снов	{леша,геи}	Леша	2022-11-20 10:55:42	458554554
92	AwACAgIAAxkBAAId_mN6B-q-n-Bs42ooSdOtuZOtfh-WAAJBJgAC2HUYSWrA8cosfdmfKwQ	ПАКА	Глеб со всеми здоровается	{глеб,классика}	Глеб	2022-11-20 10:57:00	458554554
93	AwACAgIAAxkBAAIeDGN6CBmjIAn3jahWkaHyTNBNu8q9AALJIQACCERISYKsDzh0gEJ-KwQ	Борьба с собой	Леша бореться со своей шизофренией	{леша,шиза,классика}	Леша	2022-11-20 10:57:53	458554554
94	AwACAgIAAxkBAAIeGmN6CD3mDvPetIo5Ut1VZrDhTbD3AALpHQACCCaoSd9a2VvRh4eSKwQ	На кнопку блять жми	...	{леша,классика,шиза}	Леша	2022-11-20 10:58:22	458554554
95	AwACAgIAAxkBAAIeKGN6CHAgfFa39N_gVvLj6nM_4J_FAAITJwACVQgBSouJARAacNWNKwQ	Полоскание	...	{леша,шизозвуки,классика}	Леша	2022-11-20 10:59:13	458554554
96	AwACAgIAAxkBAAIeNmN6CJiqh4QBNnaT8usrPMNFBC4RAALSGAACQttRS6Reldrmafr9KwQ	Скатина ты поганая	Егор ругается	{егор,ругательства}	Егор	2022-11-20 10:59:50	458554554
97	AwACAgIAAxkBAAIeRGN6CQVqAkidQigSsdk8M9t71NfXAAJIHwAC8f2wShtzMP4EdMojKwQ	ржут	7 человек в одном голосовм	{леша,шизозвуки,шиза,классика}	Леша	2022-11-20 11:01:57	458554554
98	AwACAgIAAxkBAAIeUmN6CUTzN7jA50AEIrV2sZpV2lCzAAIsHwACX7_ZSoUjmiIdGKaGKwQ	Сцепление	Шиза от Илющи	{илья,шиза}	Илья	2022-11-20 11:02:45	458554554
99	AwACAgIAAxkBAAIeYGN6CWkj12rQHzl1upydoElT6NqVAAIkHwACX7_ZSkmFVGhifU5XKwQ	Все хотят меня убить	...	{илья,классика,шиза}	Илья	2022-11-20 11:03:25	458554554
100	AwACAgIAAxkBAAIebmN6CYUDXHpK8_z0Qv4wzlBYwlYpAAI_IgACIzkhS2eKNndVIoq0KwQ	Сам ты гей	Сам ты гей иди в жопу	{илья,ругательства}	Илья	2022-11-20 11:03:53	458554554
101	AwACAgIAAxkBAAIfJWOgor6JSTSa345pFJIgxL_1eLUzAAIsJwACyoh4SPPjT3weuVppLAQ	Аладушек, пирожочек, цветочек	Аладушек пирожочек цветочек все в рифму	{илья,классика}	Илья	2022-12-19 17:44:23	458554554
102	AwACAgIAAxkBAAIfM2OgowEbl1cCJul0uSt47dnGXDrVAAIRJAACkMyISFv8cS0boOulLAQ	Ты чё бредишь	Ты чё бредишь	{леха,классика}	Леша	2022-12-19 17:44:58	458554554
103	AwACAgIAAxkBAAIfRWOh2dPBRtKt_02cpDfvUwG18TCBAAJDIgAC-z4JSUWwSy0whMOlLAQ	Я хочу жизофрению	Илюша на жизе	{илья,классика}	Илья	2022-12-20 15:51:12	458554554
104	AwACAgIAAxkBAAIfU2Oh2fpLWKfZb_xR_HmwbxeVlPpsAAJEIgAC-z4JSSH4o9Rb_ElwLAQ	Хуй на блюде какие люди	Хуй на блюде какие люди	{илья,классика}	Илья	2022-12-20 15:51:47	458554554
105	AwACAgIAAxkBAAIfYWOh3QQHsj4J1myuY4UvkzWowqT2AALuJQACFoURSRvUTdlCFYtVLAQ	Клоун	Ебат ты клоун	{илья,оскорбление}	Илья	2022-12-20 16:04:41	458554554
106	AwACAgIAAxkBAAIfb2Oi5HN_64o1TrlFgOzIdWIS3YnhAAKQIgAC0ZoYSVoyeT-s54HiLAQ	Ты че мне блять тут устроил	Егор ругается	{егор,ругательства}	Егор	2022-12-21 10:48:40	458554554
107	AwACAgIAAxkBAAIfrWOjD3krj9FmB7F8a4cwhB8k9E3DAALdKQACw30YSd5BPi8YLzThLAQ	Клуб домосенок	гомосенок	{серик,классика}	Серик	2022-12-21 13:52:29	458554554
\.


--
-- Name: voicestickers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres_voicestickers
--

SELECT pg_catalog.setval('public.voicestickers_id_seq', 107, true);


--
-- PostgreSQL database dump complete
--

