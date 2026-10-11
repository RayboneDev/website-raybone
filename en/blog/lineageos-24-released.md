---
layout: post
lang: en
section: blog
title: LineageOS 24 released
excerpt: A look at the changes in the latest version of LineageOS
permalink: /en/blog/lineageos-24-released/
translation_url: /blog/lineageos-24-released/
date: 2026-10-11
author: Amirali Akbari
---

LineageOS 24 was released on October 11, 2026. It is based on Android 17, which was released in July this year. This release arrives as the project approaches its tenth anniversary.

<figure class="post-lead-image">
  <img src="{{ '/assets/images/blog/lineageos-24-released.webp' | relative_url }}" alt="LineageOS 24 artwork showing Android 17, Canvas, streamed updates, and WebUSB flashing" width="1440" height="811">
</figure>

Alongside Android security patches, LineageOS 24 includes newer versions of its apps. Catapult (the smart TV launcher), Etar (calendar), Twelve (music player), Seedvault (the system backup tool), and the system WebView have all been updated. Many LineageOS apps have also been redesigned with Material 3.

This release introduces Canvas as a new photo editor. The Jelly browser can now create website shortcuts that behave like progressive web apps. SetupWizard has a more modern design and a new architecture for the initial setup process, including support for device-specific pages.

The system updater now receives releases as a stream, reducing the time needed to install a new version. Its interface has also improved and can show release notes to users. On devices that do not support A/B updates, the recovery partition updates automatically after the first successful boot following an update. The updater also uses Material 3 and has a better layout on tablets and TVs.

Starting with this release, the LineageOS online flashing tool can be used to install builds more easily on phones via WebUSB.

The a11y project has also tested the setup flow and LineageOS apps for accessibility, helping make LineageOS available to more people with different access needs.

From version 24 onward, LineageOS strongly recommends against using old kernel versions, including 4.4 and 4.9, for devices.

Many phones can already be upgraded to LineageOS 24. For more information, see the [release changelog](https://lineageos.org/Changelog-32/).
