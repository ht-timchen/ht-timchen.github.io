---
layout: page
title: "Publications"
---

<div id="tag-filter-container" style="margin-bottom: 30px;">
  <div style="margin-bottom: 15px;">
    <strong>Filter by tags:</strong>
  </div>
  <div id="tag-buttons" style="margin-bottom: 15px;">
    <button class="tag-filter-btn" data-tag="AI" id="tag_AI" style="margin: 5px; padding: 8px 15px; border: 1px solid #F2D4D7; background-color: #F2D4D7; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">AI</button>
    <button class="tag-filter-btn" data-tag="Medical" id="tag_Medical" style="margin: 5px; padding: 8px 15px; border: 1px solid #C8E6D4; background-color: #C8E6D4; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">Medical</button>
    <button class="tag-filter-btn" data-tag="XR" id="tag_XR" style="margin: 5px; padding: 8px 15px; border: 1px solid #F5E6A3; background-color: #F5E6A3; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">XR</button>
    <button class="tag-filter-btn" data-tag="BCI" id="tag_BCI" style="margin: 5px; padding: 8px 15px; border: 1px solid #B8E2D8; background-color: #B8E2D8; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">BCI</button>
    <button class="tag-filter-btn" data-tag="Fabrication" id="tag_Fabrication" style="margin: 5px; padding: 8px 15px; border: 1px solid #C4C5E8; background-color: #C4C5E8; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">Fabrication</button>
    <button class="tag-filter-btn" data-tag="Graphics" id="tag_Graphics" style="margin: 5px; padding: 8px 15px; border: 1px solid #E6D4E8; background-color: #E6D4E8; border-radius: 4px; cursor: pointer; font-size: 14px; color: #333;">Graphics</button>
    <button id="clear-filter-btn" style="margin: 5px; padding: 8px 15px; border: 1px solid #999; background-color: #f5f5f5; color: #333; border-radius: 4px; cursor: pointer; font-size: 14px;">Clear Filter</button>
  </div>
</div>
<style>
.tag-filter-btn {
  transition: all 0.2s ease;
  position: relative;
}

.tag-filter-btn.active {
  opacity: 1 !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
  transform: scale(1.08) !important;
  border-width: 2px !important;
  border-color: #333 !important;
  font-weight: 600 !important;
}

.tag-filter-btn:not(.active) {
  opacity: 0.7;
}

.tag-filter-btn:hover:not(.active) {
  opacity: 1 !important;
  transform: scale(1.05);
}

.tag-filter-btn:hover.active {
  transform: scale(1.1) !important;
}

.paper-tag {
  display: inline-block;
  margin: 3px 5px 3px 0;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  color: #333;
  font-weight: 500;
}

.paper-row {
  transition: opacity 0.3s ease;
}

.paper-row.hidden {
  display: none;
}
</style>
<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<tbody>
<tr class="paper-row" data-tags="AI Medical">
<td><img src="/assets/img/2026_ISBI_L2D.jpg" width="250"></td><td markdown="span">**Understanding Annotation Error Propagation and Learning an Adaptive Policy for Expert Intervention in Barrett's Video Segmentation**<br><br>Lokesha Rasanjalee, Dileepa Pitawela, Jin Tan, Rajvinder Singh, **Tim Chen**<br>*International Symposium on Biomedical Imaging (ISBI)* 2026<br><a href="/assets/publications/2026_ISBI_L2D.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #C8E6D4; border: 1px solid #C8E6D4;">Medical</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics XR">
<td><img src="/assets/img/2026_EG_OUGS.jpg" width="250"></td><td markdown="span">**OUGS: Active View Selection via Object-aware Uncertainty Estimation in 3DGS**<br><br>Haiyi Li, Qi Chen, Denis Kalkofe, **Tim Chen**<br>*Eurographics* 2026<br><a href="/assets/publications/2026_EG_OUGS.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2026_TVCG_Cybersickness.jpg" width="250"></td><td markdown="span">**Kinematic Sickness: Understanding Cybersickness Through Body Kinematics**<br><br>Carlos Tirado Cortes, Yiheng Chi, Juno Kim, **Tim Chen**<br>*Transaction on Visualisation and Computer Graphics (IEEE VR)* 2026<br><a href="/assets/publications/2026_TVCG_Cybersickness.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="AI">
<td><img src="/assets/img/2025_Access_L2CU.jpg" width="250"></td><td markdown="span">**L2CU: Learning to Complement Unseen Users**<br><br>Dileepa Pitawela, Gustavo Carneiro, **Tim Chen**<br>*IEEE Access* 2026<br><a href="/assets/publications/2025_Access_L2CU.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span></td>
</tr>
<tr class="paper-row" data-tags="AI">
<td><img src="/assets/img/2025_DICTA_L2D.jpg" width="250"></td><td markdown="span">**Learning To Defer To A Population With Limited Demonstrations**<br><br>Nilesh Ramgolam, Gustavo Carneiro, **Tim Chen**<br>*DICTA* 2025<br><a href="/assets/publications/2025_DICTA_L2D.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span></td>
</tr>
<tr class="paper-row" data-tags="AI Medical">
<td><img src="/assets/img/2025_CVPR_Ordinal.png" width="250"></td><td markdown="span">**CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss**<br><br>Dileepa Pitawela, Gustavo Carneiro, **Tim Chen**<br>*CVPR* 2025<br><a href="/assets/publications/2025_CVPR_CLOC.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #C8E6D4; border: 1px solid #C8E6D4;">Medical</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2025_CHI_LM.jpg" width="250"></td><td markdown="span">**A Longitudinal Study on The Effects of Circadian Fatigue on Sound Source Identification and Localization using Heads-Up Displays**<br><br>Alexander G. Minton, Howe Yuan Zhu, **Tim Chen**, Yu-Kai Wang, Zhuoli Zhuang, Gina Notaro, Raquel Galvan, James Allen, Matthias D. Ziegler, Chin-Teng Lin<br>*CHI* 2025<br><a href="/assets/publications/2025_CHI_fatigue.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/aXunoZZKcs4" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2025_CHI_XRAuthor.jpg" width="250"></td><td markdown="span">**Educator Perceptions of XRAuthor: An Accessible Tool for Authoring Learning Content with Different Immersion Levels**<br><br>Songjia Shen, Chek Tien Tan, **Tim Chen**, William L. Raffe, Tuck Wah Leong<br>*CHI* 2025<br><a href="/assets/publications/2025_CHI_XRAuthor.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/PnblYeE9gbs" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="AI Medical">
<td><img src="/assets/img/2025_CHIW_AI-Colonoscopy.png" width="250"></td><td markdown="span">**Toward a Human-Centered AI-assisted Colonoscopy System in Australia**<br><br>**Tim Chen**, Yuan Zhang, Gustavo Carneiro, Rajvinder Singh<br>*CHI Interactive Health Workshop* 2025<br><a href="/assets/publications/2025_CHIW_AI-Colonoscopy.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #C8E6D4; border: 1px solid #C8E6D4;">Medical</span></td>
</tr>
<tr class="paper-row" data-tags="AI">
<td><img src="/assets/img/2025_HCII_SnapCode.png" width="250"></td><td markdown="span">**SnapNCode: An Integrated Development Environment for Programming Physical Objects Interactions**<br><br>Xiaoyan Wei, Zijian Yue, **Tim Chen**<br>*HCII* 2025<br><a href="/assets/publications/2025_HCII_SnapCode.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span></td>
</tr>
<tr class="paper-row" data-tags="AI">
<td><img src="/assets/img/2025_HCII_CAT.png" width="250"></td><td markdown="span">**Context-AI Tunes: Context-Aware AI-Generated Music for Stress Reduction**<br><br>Xiaoyan Wei, Zebang Zhang, Zijian Yue, **Tim Chen**<br>*HCII* 2025<br><a href="/assets/publications/2025_HCII_CAT.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span></td>
</tr>
<tr class="paper-row" data-tags="AI XR">
<td><img src="/assets/img/2024_AAAI_SBV.png" width="250"></td><td markdown="span">**Segment beyond View: Handling Partially Missing Modality for Audio-Visual**<br><br>Renjie Wu, Hu Wang, Feras Dayoub, and **Tim Chen**<br>*AAAI* 2024<br><a href="/assets/publications/2024_AAAI_SBV.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="AI">
<td><img src="/assets/img/2024_AAAI_WebVLN.png" width="250"></td><td markdown="span">**WebVLN: Vision-and-Language Navigation on Websites**<br><br>Qi Chen, Dileepa Pitawela, Gengze Zhou, **Tim Chen**, and Qi Wu<br>*AAAI* 2024<br><a href="/assets/publications/2024_AAAI_WebVLN.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span></td>
</tr>
<tr class="paper-row" data-tags="AI Medical">
<td><img src="/assets/img/2024_ISBI_IQA.png" width="250"></td><td markdown="span">**Learning Subjective Image Quality Assessment for Transvaginal Ultrasound Scans from Multi-Annotator Labels**<br><br>Daniel Petashvili, Hu Wang, Alison Deslandes, Jodie Avery, George Condous, Gustavo Carneiro, Mary Hull, **Tim Chen**<br>*ISBI* 2024<br><a href="/assets/publications/2024_ISBI_TVUS.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #C8E6D4; border: 1px solid #C8E6D4;">Medical</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2024_PLOS_P300.png" width="250"></td><td markdown="span">**Understanding the effects of stress on the P300 response during naturalistic simulation of heights exposure**<br><br>Howe Yuan Zhu, **Tim Chen**, Chin-Teng Lin<br>*PLOS One* 2024<br><a href="/assets/publications/2024_PLOS_P300.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2023_ISMAR_Mismatch.png" width="250"></td><td markdown="span">**The Effect of Visual and Auditory Modality Mismatching between Distraction and Warning on Pedestrian Street Crossing Behavior**<br><br>Renjie Wu, and  **Tim Chen**<br>*IEEE ISMAR* 2023<br><a href="/assets/publications/2023_ISMAR_Mismatch.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/0hMG3Ra4XE8" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2023_VR_Sickness.png" width="250"></td><td markdown="span">**An EEG-based Experiment on VR Sickness and Postural Instability While Walking in Virtual Environments**<br><br>Carlos A. Tirado Cortes, Chin-Teng Lin, Tien-Thong Nguyen Do, and **Tim Chen**<br>*IEEE VR* 2023<br><a href="/assets/publications/2023_VR_Sickness.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/c5vwmdgTReA" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="AI Medical">
<td><img src="/assets/img/2022_ISBI_Track.png" width="250"></td><td markdown="span">**In Defense of Kalman Filtering for Polyp Tracking from Colonoscopy Videos**<br><br>David Butler, Yuan Zhang, **Tim Chen**, Seon Ho Shin, Rajvinder Singh, and Gustavo Carneiro<br>*IEEE ISBI* 2022<br><a href="/assets/publications/2022_ISBI_Track.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F2D4D7; border: 1px solid #F2D4D7;">AI</span><span class="paper-tag" style="background-color: #C8E6D4; border: 1px solid #C8E6D4;">Medical</span></td>
</tr>
<tr class="paper-row" data-tags="BCI">
<td><img src="/assets/img/2022_JNE_Shared.jpg" width="250"></td><td markdown="span">**Error-related potential-based shared autonomy via deep recurrent reinforcement learning**<br><br>Xiaofei Wang, **Tim Chen**, and Chin-Teng Lin<br>*Journal of Neural Engineering* 2022<br><a href="/assets/publications/2022_JNE_shared autonomy.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2021_TVCG_VRPlank.jpg" width="250"></td><td markdown="span">**The Effects of Virtual and Physical Elevation on Physiological Stress during Virtual Reality Height Exposure**<br><br>Howe Yuan Zhu, **Tim Chen**, and Chin-Teng Lin<br>*IEEE Trans. on Visualization and Computer Graphics* 2021<br><a href="/assets/publications/2021_TVCG_VRPlank.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/3PupSWZg55I" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2021_Frontier_Assembly.jpg" width="250"></td><td markdown="span">**Effects of Level of Immersion on Virtual Training Transfer of Bimanual Assembly Tasks**<br><br>Songjia Shen, **Tim Chen**, William Raffe, and Tuck Wah Leong<br>*Frontiers in VR* 2021<br><a href="/assets/publications/2021_Frontier_Assembly.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/wdodl_YrNzs" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2021_CHIEA_Drone.jpg" width="250"></td><td markdown="span">**A Drone Nearly Hit Me! A Reflection on the Human Factors of Drone Collisions**<br><br>Howe Yuan Zhu, Eirene Margaret Magsino, Sanjid Mahmood Hamim, Chin-Teng Lin, and **Tim Chen**<br>*ACM CHI EA* 2021<br><a href="/assets/publications/2021_CHIEA_Drone.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/xAMALgG8w7w" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2020_neuroimage.jpg" width="250"></td><td markdown="span">**The Impact of Hand Movement Velocity on Cognitive Conflict Processing in a 3D Object Selection Task in Virtual Reality**<br><br>Avinash K. Singh, Klaus Gramann, **Tim Chen**, and Chin-Teng Lin<br>*NeuroImage (h5-i=115)* 2020<br><a href="/assets/publications/2020_Neuroimage.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/PffvKv9H6ac" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2020_TCDS.jpg" width="250"></td><td markdown="span">**Intra-individual Completion Time Modulates the Prediction Error Negativity in a Virtual 3D Object Selection Task**<br><br>Avinash K. Singh, **Tim Chen**, Klaus Gramann, and Chin-Teng Lin<br>*IEEE Trans. on Cognitive and Developmental Systems* 2020<br><a href="/assets/publications/2020_TCDS_conflict.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2019_VR_Fall.jpg" width="250"></td><td markdown="span">**Evaluating Balance Recovery Techniques for Users Wearing Head-Mounted Display in VR**<br><br>Carlos A. Tirado Cortes, **Tim Chen**, Daina Sturnieks, Jaime Garcia, Stephen Lord, and Chin-Teng Lin<br>*IEEE Trans. on Visualization and Computer Graphics* 2019<br><a href="/assets/publications/2019_TVCG_VR Fall.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/ERDrDeeRvYQ" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2019_VRCAI.jpg" width="250"></td><td markdown="span">**Analysis of VR Sickness and Gait Parameters During Non-Isometric Virtual Walking with Large Translational Gain**<br><br>Carlos A. Tirado Cortes, **Tim Chen**, and Chin-Teng Lin<br>*ACM SIGGRPAH VRCAI* 2019<br><a href="/assets/publications/2019_VRCAI_sickness.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2019_CHI.jpg" width="250"></td><td markdown="span">**Towards a Complementary Metric of Haptic Immersion in VR using Event-Related Brain Potentials**<br><br>Lukas Gehrke, Sezen Akman, Pedro Lopes, Albert Chen, Avinash Kumar Singh, **Tim Chen**, Chin-Teng Lin, Klaus Gramann.<br>*ACM CHI* 2019<br><a href="/assets/publications/2019_CHI_HapticImmersion.pdf" target="_blank">[paper]</a>   <br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="BCI XR">
<td><img src="/assets/img/2018_Access.jpg" width="250"></td><td markdown="span">**Visual Appearance Modulates Prediction Error in Virtual Reality**<br><br>Avinash K. Singh, **Tim Chen**, Yu-Feng Cheng, Jung-Tai King, Li-Wei Ko, Klaus Gramann, and Chin-Teng Lin<br>*IEEE Access* 2018<br><a href="/assets/publications/2018_ACCESS_PredictionError.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/E7w3Z4u1oB0" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #B8E2D8; border: 1px solid #B8E2D8;">BCI</span><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="Fabrication">
<td><img src="/assets/img/2017_TrussFab.jpg" width="250"></td><td markdown="span">**TrussFab: Fabricating Sturdy Large-Scale Structures on Desktop 3D Printers**<br><br>Robert Kovacs, Anna Seufert, Ludwig Wall, **Tim Chen**, Florian Meinel, Willi Müller, Si-jing You, Maximilian Brehm, Jonathan Striebel, Yannis Kommana, Alexander Popiak, Thomas Bläsius, and Patrick Baudisch<br>*ACM CHI* 2017<br><a href="/assets/publications/2017_CHI_TrussFab.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/aoSzOL9k990" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #C4C5E8; border: 1px solid #C4C5E8;">Fabrication</span></td>
</tr>
<tr class="paper-row" data-tags="Fabrication">
<td><img src="/assets/img/2016_MetaMaterial.png" width="250"></td><td markdown="span">**Metamaterial Mechanisms**<br><br>Alexandra Ion, Johannes Frohnhofen, Ludwig Wall, Robert Kovacs, Mirela Alistar,  Jack Lindsay,  Pedro Lopes, **Tim Chen**, and Patrick Baudisch<br>*ACM UIST* 2016<br><a href="/assets/publications/2016_UIST_Metamaterial.pdf" target="_blank">[paper]</a>  <a href="https://www.youtube.com/watch?v=lsTiWYSfPck" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #C4C5E8; border: 1px solid #C4C5E8;">Fabrication</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2016_IconSet.png" width="250"></td><td markdown="span">**Icon Set Selection via Human Computation**<br><br>Lasse Laursen,  Yuki Koyama,  **Tim Chen**,  Elena Garces,  Diego Gutierrez, Richard Harper,  Takeo Igarashi<br>*Pacific Graphics* 2016<br><a href="/assets/publications/2016_PG_icon.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/bGmqtp76Me0" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2016_DataDrivenHistory.jpg" width="250"></td><td markdown="span">**Data-driven History List for Image Editing**<br><br>**Tim Chen**,  Li-Yi Wei,  Björn Hartmann,  and Maneesh Agrawala<br>*ACM I3D* 2016<br><a href="/assets/publications/2016_I3D_history.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/Cb89iqSRBpw" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
<tr class="paper-row" data-tags="Fabrication">
<td><img src="/assets/img/2015_LasterStacker.jpg" width="250"></td><td markdown="span">**LaserStacker: Creating Non-Planar Objects using a Laser Cutter Without Need for Manual Assembly**<br><br>Udayan Umapathi,  **Tim Chen**,  Stefanie Mueller, Ludwig Wall, Anna Seufert, and Patrick Baudisch<br>*ACM UIST* 2015<br><a href="/assets/publications/2015_UIST_LaserStacker.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/puDD_CrVH7g" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #C4C5E8; border: 1px solid #C4C5E8;">Fabrication</span></td>
</tr>
<tr class="paper-row" data-tags="Fabrication">
<td><img src="/assets/img/2015_Protopiper.jpg" width="250"></td><td markdown="span">**Protopiper: Physically Sketching Room-Sized Objects at Actual Scale**<br><br>Harshit Agrawal,  Udayan Umapathi,  Robert Kovacs, Johannes Frohnhofen,  **Tim Chen**,  Stefanie Mueller,  and Patrick Baudisch<br>*ACM UIST* 2015<br><a href="/assets/publications/2015_UIST_Protopiper.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/beRA4sIjxa8" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #C4C5E8; border: 1px solid #C4C5E8;">Fabrication</span></td>
</tr>
<tr class="paper-row" data-tags="Fabrication">
<td><img src="/assets/img/2015_Platener.jpg" width="250"></td><td markdown="span">**Platener: Low-Fidelity Fabrication of 3D Objects by Substituting 3D Print with Laser-Cut Plates**<br><br>Dustin Beyer, Serafima Gurevich,  Stefanie Mueller,  **Tim Chen**,  and Patrick Baudisch<br>*ACM CHI* 2015<br><a href="/assets/publications/2015_CHI_platener.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/hxUitLZaPf4" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #C4C5E8; border: 1px solid #C4C5E8;">Fabrication</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2014_Autocomplete.jpg" width="250"></td><td markdown="span">**Autocomplete Painting Repetition**<br><br>Jun Xing,  **Tim Chen**, and Li-Yi Wei<br>*ACM Trans. on Graphics* 2014<br><a href="/assets/publications/2014_SA_Autocomplete.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/m7MEAw46Ojo" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2014_Viewpoint.jpg" width="250"></td><td markdown="span">**History Assisted View Authoring for 3D Models**<br><br>**Tim Chen**,  Tovi Grossman,  Li-Yi Wei,  Ryan Schmidt,  Bjorn Hartmann, George Fitzmaurice, and Maneesh Agrawala<br>*ACM CHI* 2014<br><a href="/assets/publications/2014_CHI_viewpoint.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/_7r-C7Eg1Pw" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
<tr class="paper-row" data-tags="XR">
<td><img src="/assets/img/2013_Faceton.jpg" width="250"></td><td markdown="span">**Facetons: Face Primitives with Adaptive Bounds for 3D Architectural Building in Virtual Environment**<br><br>Naoki Sasaki,  **Tim Chen**,  Daisuke Sakamoto, and Takeo Igarashi<br>*ACM VRST* 2013<br><a href="/assets/publications/2013_VRST_Faceton.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/G8lkQ9tLgIs" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #F5E6A3; border: 1px solid #F5E6A3;">XR</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2013_Splatter.jpg" width="250"></td><td markdown="span">**Interactive Physics-based Ink Splattering Art Creation**<br><br>Eugene Lei, Ying-Chieh Chen, Tim Chen,  and Chun-Fa Chang<br>*Computer Graphics Forum* 2013<br><a href="/assets/publications/2013_PG_Splattering.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/oWSqA3KluJA" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
<tr class="paper-row" data-tags="Graphics">
<td><img src="/assets/img/2011_rev.jpg" width="250"></td><td markdown="span">**Nonlinear Revision Control for Images**<br><br>**Tim Chen**,  Li-Yi Wei, and Chun-Fa Chang<br>*ACM Trans. on Graphics * 2011<br><a href="/assets/publications/2011_SIG_revision.pdf" target="_blank">[paper]</a>  <a href="https://youtu.be/RBL1cVzIQik" target="_blank">[youtube]</a><br><br><span class="paper-tag" style="background-color: #E6D4E8; border: 1px solid #E6D4E8;">Graphics</span></td>
</tr>
</tbody>
</table>
<script>
(function() {
  var selectedTags = new Set();
  var tagButtons = document.querySelectorAll('.tag-filter-btn');
  var clearFilterBtn = document.getElementById('clear-filter-btn');
  var paperRows = document.querySelectorAll('.paper-row');
  
  function syncButtonStates() {
    // Sync button active states with selectedTags Set
    tagButtons.forEach(function(btn) {
      var tag = btn.getAttribute('data-tag');
      if (selectedTags.has(tag)) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
    // Debug: log selected tags
    console.log('Selected tags:', Array.from(selectedTags));
  }
  
  function filterPapers() {
    if (selectedTags.size === 0) {
      paperRows.forEach(function(row) {
        row.classList.remove('hidden');
      });
    } else {
      paperRows.forEach(function(row) {
        var rowTags = row.getAttribute('data-tags').split(' ').filter(function(t) { return t.length > 0; });
        var hasMatch = false;
        
        selectedTags.forEach(function(selectedTag) {
          var selectedTagId = selectedTag.replace(/[^a-zA-Z0-9]/g, '_');
          if (rowTags.indexOf(selectedTagId) !== -1) {
            hasMatch = true;
          }
        });
        
        if (hasMatch) {
          row.classList.remove('hidden');
        } else {
          row.classList.add('hidden');
        }
      });
    }
  }
  
  // Initialize: ensure no buttons are active initially
  syncButtonStates();
  
  tagButtons.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var tag = btn.getAttribute('data-tag');
      
      // If the clicked tag is already selected, clear all filters
      if (selectedTags.has(tag)) {
        selectedTags.clear();
      } else {
        // Clear all selected tags first, then select the clicked tag
        selectedTags.clear();
        selectedTags.add(tag);
      }
      
      // Always sync ALL button states after any change
      syncButtonStates();
      filterPapers();
    });
  });
  
  clearFilterBtn.addEventListener('click', function() {
    selectedTags.clear();
    syncButtonStates();
    filterPapers();
  });
})();
</script>
