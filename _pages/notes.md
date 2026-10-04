---
layout: archive
title: "Learning Notes"
permalink: /notes/
author_profile: true
---

I publish notes as I complete work. Each post states the project stage, data source, method, evidence and limitations.

<ul>
  {% for post in site.posts %}
    <li>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d %B %Y" }}</time>{% if post.excerpt %} · {{ post.excerpt | strip_html | truncate: 180 }}{% endif %}</p>
    </li>
  {% endfor %}
</ul>
