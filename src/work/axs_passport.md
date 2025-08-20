---
logo: /img/projects/axs_passport.png
screenshot: /img/projects/axs_passport_screenshot.png
title: AXS Passport
description: As the founding software engineer, I built and scaled a comprehensive digital identity platform from MVP to production, leading an 8-person engineering team and architecting secure, scalable systems handling complex organisational hierarchies.
---

!!! info "Heads up!" Unfortunately this project had to end when the parent company
closed down. The currently live version of AXS Passport isn't the one I helped build.

AXS Passport is a sophisticated digital identity and access management platform that I
architected and developed from the ground up. Starting as the founding software
engineer, I worked closely with the product owner to transform their vision into a
functional, well-loved MVP, then scaled both the product and the engineering team to
meet growing demand.

## Technical Leadership & Team Building

I began as the sole engineer on the project and successfully scaled the development team
to 8 engineers over the course of a year. This involved not only hiring and mentoring
new team members but also establishing development practices, code standards, and
architectural patterns that enabled the team to work efficiently at scale.

Working in close partnership with the product owner, I helped refine and implement
features that balanced user needs with technical feasibility, ensuring we delivered a
product that was both innovative and maintainable.

## Backend Architecture & API Development

I designed and built the entire backend API service using **Python** and **FastAPI**,
creating a robust and secure foundation for the platform. The API incorporated
enterprise-grade features including:

- **Advanced Authentication & Authorisation**: Implemented Bearer token-based
  authentication with comprehensive Role-Based Access Control (RBAC), supporting complex
  access patterns including guest access and hierarchical organisation-based permissions
- **Performance & Reliability**: Integrated rate limiting and comprehensive logging
  using OpenTelemetry (OTEL) to enable security audits and detailed performance metrics
- **Security Excellence**: Implemented a highly secure architecture covering the OWASP
  API Security Top 10 and additional security best practices. The system underwent
  annual external security audits with no major flaws identified, and any moderate to
  minor issues were consistently resolved within 2 weeks
- **Complex Data Management**: Developed sophisticated SQL queries using recursive
  Common Table Expressions (CTEs) to efficiently handle detailed organisational
  hierarchies with nested sub-organisations
- **Database Optimisation**: Tuned a PostgreSQL database for high-performance data
  delivery, supporting complex search queries and data-intensive dashboard operations

## Frontend Development & User Experience

I built the original frontend application using **SvelteKit** and **TailwindCSS**, later
leading the team responsible for its continued development and enhancement. Key frontend
achievements include:

- **Responsive Design**: Created a mobile-first responsive interface that provides an
  excellent user experience across all devices
- **Accessibility Excellence**: Ensured high conformance to WCAG AA accessibility
  requirements, making the platform inclusive for all users
- **Dynamic Theming System**: Developed an innovative theming system allowing users to
  select any colour for personalisation whilst automatically maintaining AA contrast
  ratios for accessibility compliance. This system dynamically re-themes the entire
  interface, including the logo using inline SVGs
- **Custom QR Code Generation**: Implemented branded and themeable QR codes that
  maintain visual consistency with user-selected themes

## Mobile Application Development

I inherited and significantly enhanced a **React Native** mobile application,
modernising both its functionality and user experience:

- Refreshed the UI/UX design for improved usability and visual consistency with the web
  platform
- Implemented new sharing features that extended the platform's functionality to mobile
  users
- Ensured feature parity and seamless synchronisation between web and mobile experiences

## DevOps & Infrastructure

I established a comprehensive deployment pipeline that ensured reliable, secure
releases:

- **CI/CD Pipeline**: Created an automated deployment system using **GitHub Actions**,
  incorporating continuous integration and deployment workflows
- **Quality Assurance**: Implemented a release pipeline requiring pull request sign-off
  from senior engineers and passing test suites before deployment
- **Containerisation**: Utilised **Docker** and **Docker Compose** for consistent
  deployments across environments
- **Infrastructure Management**: Managed deployment and maintenance of **Linux/Debian**
  servers, ensuring high availability and performance
