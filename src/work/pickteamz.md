---
link: https://pickteamz.com
logo: /img/projects/pickteamz.png
screenshot: /img/projects/pickteamz_screenshot.png
title: PickTeamz
description: Architected and developed a multi-tenant fantasy football platform as sole engineer, building real-time backend systems with Django and Celery, cross-platform mobile apps with Flutter, and implementing white-label solutions for multiple clients. Delivered a complete technical solution from infrastructure to user interface, enabling thousands of players to engage with this innovative team-based fantasy sports game.
---

I partnered with founder Stuart Wakeford to bring his innovative vision to life: a
fantasy football game where players pick teams rather than individual players, making
the game more accessible and engaging for a broader audience.

## Technical Leadership

As the sole engineer on the project, I architected and implemented the entire technical
stack, from backend infrastructure to mobile applications. This comprehensive
responsibility allowed me to ensure seamless integration across all components whilst
maintaining high performance standards.

## Backend Architecture

I built a robust backend system using Django and Python, designing it to handle
real-time sports data processing at scale. The architecture incorporates Celery for
managing time-critical background tasks, ensuring that when a goal is scored, push
notifications reach users within seconds. The system utilises Redis as a message broker
and PostgreSQL for persistent data storage, creating a reliable and performant
foundation.

The infrastructure runs on Digital Ocean using Dokku for containerised deployments. I
established a continuous integration and deployment pipeline using GitHub Actions,
enabling automated testing and zero-downtime deployments with every code push.

## Multi-tenant Platform

One of the project's most interesting technical challenges was implementing a
white-label solution. I designed the system to support multiple clients, each with their
own branding, custom game rules, and tailored content. This multi-tenant architecture
shares a common data API whilst allowing complete customisation for each client's
specific requirements. This approach significantly reduced development time for new
clients whilst maintaining code quality and system stability.

## Cross-platform Mobile Development

I developed native iOS and Android applications using Flutter, implementing a hybrid
approach that wraps the web experience whilst providing native functionality where it
matters most. The applications communicate seamlessly between Flutter and JavaScript
layers through custom message passing, enabling features such as native share
functionality and app store review prompts. This architecture ensures users receive a
native app experience whilst allowing rapid feature development across all platforms.

## Frontend Development

The web interface utilises Django's templating system with Bootstrap for responsive
design, enhanced with vanilla JavaScript for interactive elements. This pragmatic
approach ensures fast page loads and excellent performance across all devices whilst
maintaining clean, maintainable code.

## Collaboration and Product Development

Working closely with Stuart, I translated product requirements and design concepts into
technical solutions that delight users. This collaboration involved regular iterations
on user experience, performance optimisation, and feature development, always focusing
on delivering value to players whilst maintaining system reliability.

The success of PickTeamz demonstrates my ability to take full ownership of complex
technical projects, from initial architecture decisions through to production deployment
and ongoing maintenance, whilst collaborating effectively with stakeholders to deliver a
product that users love.
