---
layout: home-bento
title: Hsiang-Ting (Tim) Chen
subtitle: Adelaide University
omit_page_hero: true
---

<div class="bento-grid">
  <section class="bento-cell bento-cell--md-7 bento-card" markdown="1">
I am a senior lecturer (tenured assistant professor in other systems) at the [School of Computer Science and IT](https://adelaideuni.edu.au/about/school/computer-science-information-technology/), [Adelaide University](https://www.adelaide.edu.au/). Before joining Adelaide, I had the honor of working with [Prof. Patrick Baudisch](https://hpi.de/baudisch/home.html) (HPI), [Prof. Takeo Igarashi](https://www-ui.is.s.u-tokyo.ac.jp/~takeo/) (U of Tokyo), [Prof CT Lin](https://profiles.uts.edu.au/chin-teng.lin) (UTS), and [Dr. Li-Yi Wei](https://www.liyiwei.org) (Adobe Research) across various research fields including Human-Computer Interaction, Computer Graphics, and AI/ML.
  </section>

  <section class="bento-cell bento-cell--md-5 bento-card bento-card--mission" markdown="1">
My research mission is to **augment human capabilities by engineering human-centred AI systems**. I pursue this mission by actively exploring emerging technologies to build novel interactive AI systems that empower and collaborate effectively with knowledge workers. This hands-on pursuit has led to my leadership roles in large interdisciplinary teams, including serving as the U of Adelaide research lead for the Augmenting Ability CRC and as the human-AI interface lead for the [Eureka Prize-winning](https://australian.museum/get-involved/eureka-prizes/2023-eureka-prize-winners/), MRFF-funded [IMAGENDO Project](https://imagendo.org.au/).
  </section>

  <section class="bento-cell bento-cell--md-12 bento-card bento-card--side" markdown="1">
In my limited free time, I enjoy vibe coding for fun. For example, creating the [ARC Funding Analysis](https://ht-timchen.github.io/arc-discovery-analysis/) website.
  </section>

  <section class="bento-cell bento-cell--md-12 bento-card bento-card--activities" markdown="1">
### Recent activities
{: .recent-activities}
- Mar 2026: Added an [ARC funding lead CI citation analysis](https://ht-timchen.github.io/arc-discovery-analysis/lead_ci_citations_visualization.html) into my [ARC Funding Analysis](https://ht-timchen.github.io/arc-discovery-analysis/) website.
- Feb 2026: I will serve as the paper chair for the OzCHI 2026 at Adelaide.
- Feb 2026: Haiyi's paper on using local LLM for endo report extraction was accepted as a CHI 2026 poster!
- Jan 2026: A series of works on **learning to defer** were accepted. Lokesha's paper was also selected for oral presentation at [ISBI](https://biomedicalimaging.org/2026/)!
- Jan 2026: Serve as the short form chair for the first [ACM Interactive Health](https://ih.acm.org/) conference. Look forward to seeing your works here!
- Dec 2025: Haiyi's paper on object-aware 3DGS is conditionally accepted to [Eurographics 2026](https://eg2026.github.io/)!
- Dec 2025: [Carlos](https://www.sydney.edu.au/architecture/about/our-people/academic-staff/carlos-tiradocortes.html)' paper on Kinematic Sickness is conditionally accepted to [IEEE VR 2026](https://ieeevr.org/2026/) as a TVCG journal paper!
- Nov 2025: Gave a talk on health HCI for [SIGCHI Paris Chapter](https://paris.sigchi.acm.org/) at [IRIS](https://www.isir.upmc.fr/?lang=en).
- Nov 2025: Gave two talks for [INUIT](https://labsticc.fr/en/teams/inuit) and [DSD](https://www.imt-atlantique.fr/fr/l-ecole/departements-d-enseignement-recherche/data-science) at [IMT Atlantique](https://www.imt-atlantique.fr) about human-AI collaboration.
- Nov 2025: [Jie](https://www.linkedin.com/in/jie-yang-b42615235/)'s paper on multi-view clustering is accepted to AAAI 26.
- Aug 2025: Vibe coded an ARC DP analysis website [ARC DP Analysis](https://ht-timchen.github.io/arc-discovery-analysis/)
- Apr 2025: Will serve as an AC (Health) for CHI 2026
- Feb 2025: The IMAGENDO team was awarded the [AEA Ignite Grant](https://www.aea.gov.au/news/aea-ignite-grants-support-nationally-significant-research) (~$500k)!
- Feb 2025: Dileepa's paper on contrastive learning for ordinal ranking got accepted to CVPR 2025
- Feb 2025: Will serve on the jury committee for SIGGRAPH 2025 posters
- Jan 2025: 2 papers about learning and training in VR were accepted to CHI 2025
- Dec 2024: The IMAGENDO team was awared an NHMRC idea project (10% success rate, ~$2M)!

</section>
</div>

<script>
(function() {
  document.querySelectorAll('.bento-card--activities h3.recent-activities + ul li').forEach(function(li) {
    var html = li.innerHTML;
    var idx = html.indexOf(': ');
    if (idx !== -1) {
      li.innerHTML = '<span class="activity-date">' + html.substring(0, idx) + '</span>: ' + html.substring(idx + 2);
    }
  });
})();
</script>
