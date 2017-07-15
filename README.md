# Gollahalli Website

[![codecov](https://codecov.io/gh/akshaybabloo/gollahalli-com/branch/master/graph/badge.svg)](https://codecov.io/gh/akshaybabloo/gollahalli-com)
[![Build Status](https://travis-ci.org/akshaybabloo/gollahalli-com.svg?branch=master)](https://travis-ci.org/akshaybabloo/gollahalli-com)
[![Requirements Status](https://requires.io/github/akshaybabloo/gollahalli-com/requirements.svg?branch=master)](https://requires.io/github/akshaybabloo/gollahalli-com/requirements/?branch=master)

## 1 Django Template Tags

These are the tags that were used in this project:

1. To get name

  ```python
  {{ content.get_name }}
  ```
2. To get Twitter

  ```python
  {{ content.get_twitter }}
  ```
3. To get GitHub

  ```python
  {{ content.get_github }}
  ```
4. To get Linkedin

  ```python
  {{ content.get_linkedin }}
  ```
5. To get my image

  ```
  {{ content.get_my_image | safe }}
  ```
6. To get my Bio

  ```
  {{ content.get_bio | safe }}
  ```

7. To get my skills

For Table 1

```
{% for data, key in content.get_skills.t1.items %}
  {% for data_of_key in key %}
      {% if forloop.first %}
        {{ data | title }}
      {% else %}
          {# Do something #}
      {% endif %}
        {{ data_of_key }}
  {% endfor %}
{% endfor %}
```

For Table 2

```
{% for data, key in content.get_skills.t2.items %}
  {% for data_of_key in key %}
      {% if forloop.first %}
        {{ data | title }}
      {% else %}
          {# Do something #}
      {% endif %}
        {{ data_of_key }}
  {% endfor %}
{% endfor %}
```
